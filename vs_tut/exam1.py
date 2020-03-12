import teaching

def print_student_feedback(student_info: dict, feedback_mode="normal") -> None:
    '''Print students feedback according to their grades

        Parameters
        ----------
        student_info
            A dictionary with student name as key and student grade as value
        feedback_mode
            The feedback mode, either "normal" (default) or "positive_reinforcement"

        Returns
        -------
        None
    '''
    for s_name, s_grade in student_info.items():
        s_feedback = teaching.comment_grade(s_grade, mode=feedback_mode)
        print('Feedback for {}: {}'.format(s_name, s_feedback))

if __name__ == '__main__':
    print(__name__)
    student_results = {
                'John': 3,
                'Mary': 9,
                'Peter': 5
                }
    print_student_feedback(student_results)
