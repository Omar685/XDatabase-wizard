import time

def calculate_execution_time(code: str = ...) -> None:
  """
  Calculate the execution time of a python code.

  Args:
    code: The Python code to execute.
  Returns:
    The execution time in seconds.
  """

  start = time.time()
  exec(code)
  end = time.time()
  return end - start