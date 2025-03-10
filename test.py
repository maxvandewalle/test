import asyncio
import random
import time
from functools import wraps
#run this shit
# Decorator to measure execution time
def execution_time(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = await func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"{func.__name__} executed in {end_time - start_time:.4f} seconds")
        return result
    return wrapper

# Custom exception
class RandomError(Exception):
    pass

# Asynchronous class to generate random numbers
class RandomNumberGenerator:
    def __init__(self, count):
        self.count = count

    @execution_time
    async def generate_numbers(self):
        await asyncio.sleep(1)  # Simulating a delay
        numbers = [random.randint(1, 100) for _ in range(self.count)]
        if random.choice([True, False]):
            raise RandomError("An error occurred while generating numbers.")
        return numbers

# Main function to run the async tasks
async def main():
    rng = RandomNumberGenerator(10)
    try:
        numbers = await rng.generate_numbers()
        print("Generated numbers:", numbers)
    except RandomError as e:
        print(e)

if __name__ == "__main__":
    asyncio.run(main())
