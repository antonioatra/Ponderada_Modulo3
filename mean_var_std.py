import numpy as np

def calculate(numbers):
    try:
        if len(numbers) != 9:
            raise ValueError("List must contain nine numbers.")
        calculation = np.array(numbers).reshape(3,3)
        calculations = {'mean':[calculation.mean(axis=0).tolist(),calculation.mean(axis=1).tolist(),calculation.mean().tolist()],
        'variance':[calculation.var(axis=0).tolist(),calculation.var(axis=1).tolist(),calculation.var().tolist()],
        'standard deviation':[calculation.std(axis=0).tolist(),calculation.std(axis=1).tolist(),calculation.std().tolist()],
        'max':[calculation.max(axis=0).tolist(),calculation.max(axis=1).tolist(),calculation.max().tolist()],
        'min':[calculation.min(axis=0).tolist(),calculation.min(axis=1).tolist(),calculation.min().tolist()],
        'sum':[calculation.sum(axis=0).tolist(),calculation.sum(axis=1).tolist(),calculation.sum().tolist()]}
        
        return calculations

    except ValueError:
        raise

    
