import teaching

student_results = {
            'John': 3,
            'Mary': 9,
            'Peter': 5
            }

for s_name, s_grade in student_results.items():
    s_feedback = teaching.comment_grade(s_grade, mode="positive_reinforcement")
    print('Feedback for {}: {}'.format(s_name, s_feedback))

