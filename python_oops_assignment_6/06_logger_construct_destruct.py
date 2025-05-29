class Logger:
    
    # Constructor method (runs when object is created)
    def __init__(self):
        print("🟢 Logger: Object has been created.")

    # Destructor method (runs when object is destroyed)
    def __del__(self):
        print("🔴 Logger: Object has been destroyed.")


# Example usage
print("Creating logger object...")
log = Logger()  # This will call the constructor

print("Doing something with logger...")

print("Deleting logger object...")
del log  # This will call the destructor

print("End of program.")
