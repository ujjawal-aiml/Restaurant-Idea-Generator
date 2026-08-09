import os

from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()


def _get_llm() -> ChatOpenAI:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError(
            "OPENAI_API_KEY is not set. Copy .env.example to .env and add your key."
        )
    return ChatOpenAI(model="gpt-4o-mini", temperature=0.7)


def generate_restaurant_name_and_items(cuisine: str) -> dict[str, str]:
    llm = _get_llm()
    parser = StrOutputParser()

    name_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a creative restaurant branding expert."),
            (
                "human",
                "I want to open a restaurant for {cuisine} food. "
                "Suggest one fancy, memorable name. Reply with only the name, no quotes.",
            ),
        ]
    )
    name_chain = name_prompt | llm | parser

    items_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a professional chef and menu designer."),
            (
                "human",
                "Suggest 6 menu items for a restaurant called {restaurant_name}. "
                "Return only a comma-separated list of dish names.",
            ),
        ]
    )
    items_chain = items_prompt | llm | parser

    restaurant_name = name_chain.invoke({"cuisine": cuisine})
    menu_items = items_chain.invoke({"restaurant_name": restaurant_name})

    return {
        "restaurant_name": restaurant_name.strip(),
        "menu_items": menu_items.strip(),
    }


if __name__ == "__main__":
    result = generate_restaurant_name_and_items("Italian")
    print(f"Name: {result['restaurant_name']}")
    print(f"Menu: {result['menu_items']}")
