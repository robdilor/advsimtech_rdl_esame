def progress_bar(step, total):
    step = max(0, min(step, total))
    bar = '██' * step + '░░' * (total - step)
    percentage = step / total if total else 0
    print(f'\r{bar} {percentage:.2%}', end='', flush=True)