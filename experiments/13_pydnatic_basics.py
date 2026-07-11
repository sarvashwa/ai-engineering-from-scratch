from pydantic import BaseModel, Field

class AskRequest(BaseModel):
    question: str = Field(
        min_length=5,
        max_length=500,
    )
    top_k: int = 5


request = AskRequest(question="")

print(request)
print(type(request))
print(request.question)


request2 = AskRequest(question="Hi")

print(request2)
print(type(request2))
print(request2.question)


request3 = AskRequest(question="Hello")

print(request3)
print(type(request3))
print(request3.question)


request4 = AskRequest(question="How does MongoDB store patient data?")

print(request4)
print(type(request4))
print(request4.question)

request5 = AskRequest(
    question="Hello",
    top_k="7.5"
)

print(request5)
print(type(request5))
print(request5.question)
print(request5.top_k)
print(type(request5.top_k))

request6 = AskRequest(
    question="Hello",
    top_k=7.5
)

print(request6)
print(type(request6))
print(request6.question)
print(request6.top_k)
print(type(request6.top_k))

request7 = AskRequest(
    question="Hello",
    top_k=False
)

print(request7)
print(type(request7))
print(request7.question)
print(request7.top_k)
print(type(request7.top_k))

request8 = AskRequest(
    question="Hello",
    top_k=True
)

print(request8)
print(type(request8))
print(request8.question)
print(request8.top_k)
print(type(request8.top_k))

request9 = AskRequest(
    question="Hello",
    top_k=7.0
)

print(request9)
print(type(request9))
print(request9.question)
print(request9.top_k)
print(type(request9.top_k))