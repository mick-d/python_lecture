def comment_grade(grade: int, mode: str = 'normal') -> str:
    ''' Provide a feedback according to the grade value
    
        Parameters
        ----------
        grade
            The amount of distance traveled
        mode
            The feedback mode, either "normal" (default) or "positive_reinforcement"

        Returns
        -------
        comment
            The grade feedback
    '''
    if grade < 5:
        return('Grade too low')
    elif grade >= 5:
        if mode == 'normal':
            return('Grade high enough')
        elif mode == 'positive_reinforcement':
            return('Well done, keep going!')

a = 'string'
