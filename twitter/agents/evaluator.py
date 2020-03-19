from agents import Agent
from envs import CorpusController


class Evaluator(Agent):

    def __init__(self, target_path):
        super().__init__(target_path)

    def run(self, database: CorpusController, vocabulary):
        output_directory = self._target_path[:self._target_path.rfind('/') + 1]
        file_path_suffix = '_%s_%s_%s.txt' % \
                           (str(vocabulary),
                            vocabulary.window_size,
                            database.smoothing_value)

        trace_path = '%strace%s' % (output_directory, file_path_suffix)
        eval_path = '%seval%s' % (output_directory, file_path_suffix)

        languages = database.languages

        general_buffer = []
        precision_buffer = []
        recall_buffer = []
        f1_score_buffer = []

        macro_f1 = 0.0
        weighted_f1 = 0.0
        accuracy = [0.0, 0.0]

        precision = {}
        recall = {}
        frequency = {}
        for language in languages:
            precision[language] = [0.0, 0.0]
            recall[language] = [0.0, 0.0]
            frequency[language] = 0.0

        tests = vocabulary.load(self._target_path)

        for content in tests:
            if not content:
                continue

            results = database.classify(content[3])
            score, predicted_language = results

            reward = 1 if content[2] == predicted_language else 0

            precision[predicted_language][1] += 1
            precision[predicted_language][0] += reward

            recall[predicted_language][0] += reward
            recall[content[2]][1] += 1

            accuracy[0] += reward
            accuracy[1] += 1

            frequency[content[2]] += 1

            reward = 'correct' if reward == 1 else 'incorrect'
            general_buffer.append('%s  %s  %s  %s  %s' %
                                  (content[0], predicted_language,
                                   format(score, '1.2e'),
                                   content[2], reward))

        with open(trace_path, 'w') as writer:
            writer.write('\r\n'.join(general_buffer))

        general_buffer.clear()

        for language in languages:
            r_numerator, r_denominator = recall[language]
            p_numerator, p_denominator = precision[language]

            try:
                total_recall = r_numerator / r_denominator
            except ZeroDivisionError:
                total_recall = 0.0

            try:
                total_precision = p_numerator / p_denominator
            except ZeroDivisionError:
                total_precision = 0.0

            try:
                f1_score = 2 * total_recall * total_precision / (total_recall + total_precision)
            except ZeroDivisionError:
                f1_score = 0.0

            recall_buffer.append(format(total_recall, '.4f'))
            precision_buffer.append(format(total_precision, '.4f'))
            f1_score_buffer.append(format(f1_score, '.4f'))
            macro_f1 += f1_score
            weighted_f1 += f1_score * frequency[language]

        macro_f1 /= len(languages)
        weighted_f1 /= sum(frequency.values())

        general_buffer.append(format(accuracy[0] / accuracy[1], '.4f'))
        general_buffer.append('  '.join(precision_buffer))
        general_buffer.append('  '.join(recall_buffer))
        general_buffer.append('  '.join(f1_score_buffer))
        general_buffer.append('%.4f  %.4f' % (macro_f1, weighted_f1))

        with open(eval_path, 'w') as writer:
            writer.write('\r\n'.join(general_buffer))
