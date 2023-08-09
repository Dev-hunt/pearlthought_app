def test_hello_world():
    from pearlthought_app.app import main
    assert callable(main), "main function is not defined"
    
    # Capture stdout to check if the output matches
    from io import StringIO
    import sys
    original_stdout = sys.stdout
    sys.stdout = StringIO()
    
    main()
    
    output = sys.stdout.getvalue().strip()
    sys.stdout = original_stdout
    
    assert output == "Hello, World!", f"Expected 'Hello, World!', but got '{output}'"