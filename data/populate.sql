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
        'Flow Control & Object Oriented Programming',
        , ''
        , FALSE
    ),
	-- (
    --     3,
    --     'Python Modules, Frameworks, and Libraries',
    --     , ''
    --     , FALSE  
    -- ),
	-- (
    --     4,
    --     'Python advanced topics and file handling',
    --     , ''
    --     , FALSE
    -- ),
	-- (
    --     5,
    --     'Data Science Introduction using Python',
    --     , ''
    --     , FALSE
    -- ),
	-- (
    --     6,
    --     'Advanced Python with Code Introspection',
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

-- INSERT INTO session_topic(name, session_id) VALUES
--     ('', 2)

INSERT INTO session_solution(name, topic_id, solution) VALUES
    (
        'data-types-exercise'
        , 5
        , 'patient_name = "John Smith"'||E'\n'||
          'patient_age = 20'||E'\n'||
          'new_patient = True'
    );
