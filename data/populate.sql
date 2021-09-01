INSERT INTO session_session(id, name, description, enabled) VALUES
    (
        1,
        'Introduction to Python & Programming in General'
        , 'What is programming and what should you learn it? Learn about its applications and fundamentals. '
          'Students at the end of this session will learn how to perform and write basic programs using the '
          'Python strings, variables, functions, and other data types. '
        , TRUE
    );
	(
        2,
        'Further introduction to Python programming'
        , 'Students at the end of this session will learn class methods, functions, '
          'python operators, conditionals, and loops. They will also be introduced with new '
          'Python sequence data types. Such as list, range and tuples.'
        , TRUE
    ),
	(
        3,
        'Intermediate Python'
        , 'Students will learn more complex concepts such as infinite loops, nested loops, and '
          'mathematic functions in Python!'
        , TRUE
    ),
	(
        4,
        'Multiplication Table Project'
        , 'Students will make a project based on real-world applications'
        , TRUE
    ),
	-- (
    --     5,
    --     'Data Science Introduction using Python'
    --     , ''
    --     , FALSE
    -- ),
	-- (
    --     6,
    --     'Advanced Python with Code Introspection'
    --     , ''
    --     , FALSE
    -- );

INSERT INTO session_topic(name, session_id) VALUES
    ('Introduction', 1),
    ('Interacting with Python', 1),
    ('Variables and Strings', 1),
    ('Comments', 1),
    ('Data Types', 1),
    ('Builtin Functions', 1),
    ('Type Conversion', 1);

INSERT INTO session_topic(name, session_id) VALUES
    ('String Methods', 2),
    ('Python Operators', 2),
    ('Conditionals', 2),
    ('Python functions', 2),
    ('Sequence Data Types: List', 2),
    ('Sequence Data Types: Tuples', 2),
    ('Loops', 2),
    ('Sequence Data Types: Range', 2);

INSERT INTO session_topic(name, session_id) VALUES
    ('Escape Characters', 3),
    ('Formatting Strings', 3),
    ('Keyword Arguments', 3),
    ('More Data Types', 3),
    ('Infinite Loops', 3),
    ('Nested Loops', 3),
    ('Python Math', 3),
    ('Return Keyword', 3),
    ('Unpacking', 3);

INSERT INTO session_topic(name, session_id) VALUES
    ('Multiplication Project', 4);

INSERT INTO session_solution(name, topic_id, solution) VALUES
    (
        'data-types-exercise'
        , 5
        , 'patient_name = "John Smith"'||E'\n'||
          'patient_age = 20'||E'\n'||
          'new_patient = True'
    ),
    (
        'multiplication-project'
        , 57
        ,   'from random import randint'||E'\n\n'||
            'def generate_question():'||E'\n'||
            '    return tuple(randint(0, 10) for _ in range(2))'||E'\n\n'||
            'def quiz(questions):'||E'\n'||
            '    marks = 0'||E'\n\n'||
            '    for _ in range(questions):'||E'\n'||
            '        question = generate_question()'||E'\n'||
            '        formatted_question = f"{question[0]} x {question[1]}"'||E'\n'||
            '        answer = question[0] * question[1]'||E'\n\n'||
            '        user_input = int(input("What is {}? ".format(formatted_question)))'||E'\n\n'||
            '        if user_input == answer:'||E'\n'||
            '            # user answered question correctly!'||E'\n'||
            '            marks += 1'||E'\n\n'||
            '    # quiz ended'||E'\n'||
            '    print("You scored {}/{}".format(marks, questions))'||E'\n\n'||
            'def run():'||E'\n'||
            '    while True:'||E'\n'||
            '        questions = int(input("How many questions multiplication questions do you want? "))'||E'\n\n'||
            '        if questions < 3:'||E'\n'||
            '            print("That is not enough questions! Try again.")'||E'\n'||
            '        else:'||E'\n'||
            '            quiz(questions)'||E'\n'||
            '            break'||E'\n\n'||
            '# start the program'||E'\n'||
            '# run()'
    );