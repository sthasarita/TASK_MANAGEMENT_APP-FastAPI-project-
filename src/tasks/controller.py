def create_task(body):
    print(body)
    body = body.model_dump()
    print(body)
    return {"status" : "Task Created Successfully.", "task" : body}