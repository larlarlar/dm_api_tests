def attempt(
        n=5,
):
    def decorator(
            func,
    ):
        def wraps(
                *args,
                **kwargs,
        ):
            print('_____________')
            print(n)
            func(*args, **kwargs)
            print('-------------')
            return

        return wraps

    return decorator


@attempt(n=5)
def my_print(
        name,
):
    print(f"Hello, {name}1!")


@attempt(n=5)
def my_print1(
        name,
):
    print(f"Hello, {name}2!")


@attempt(n=5)
def my_print2(
        name,
):
    print(f"Hello, {name}3!")


@attempt(n=5)
def my_print3(
        name,
):
    print(f"Hello, {name}4!")


my_print(name='Mesrop')
my_print1(name='Astghik')
my_print2(name='Nebojsa')
my_print3(name='Milica')
