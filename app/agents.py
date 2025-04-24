class Refiner:
    def refine(self, query):
        return query

class Retriever:
    def retrieve(self, query):
        return {"service": "подвеска", "price": "от 3500 ₽"}

class Planner:
    def plan(self, context):
        return f"Запишем вас в филиал: {context.get('branch')}"
