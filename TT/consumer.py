import trace

def example_function():
    for i in range(1,8):
        if i%4 == 0:
            break
        else:
            print(i,end =",")

tracer = trace.Trace(count=True, trace=True)
tracer.runfunc(example_function)