def test_function():
    def inert_function():
        print('Я в области видимости функции test_function')
    inert_function()
test_function()
# inert_function() - NameError: name 'inert_function' is not defined. Did you mean: 'test_function'?
