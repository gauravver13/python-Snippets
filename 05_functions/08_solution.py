def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name="Ironman", power="ai")
print_kwargs(name="Spiderman", power="Web")
print_kwargs(name="Dr Strange", power="Time Travel")

