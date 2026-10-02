import aiohttp
import asyncio

from datetime import datetime

class BirthdayHandler:
    WEBSITE_URL = 'https://senestre-coquecigrues.fr/members/birthdays'
    MSG_WRONG_FORMAT = "Veuillez suivre le format suivant : AAAA-MM-JJ."
    MSG_BAD_ANSWER = "Le site ne me répond pas. C'EST BIEN LA PEINE DE TANT BOSSER DESSUS, SEN"
    MSG_ALL_OKAY = "Votre anniversaire est bien enregistré !! :D :D"

    async def send_birthday(member_id, birthday):
        birthday = birthday.replace("/", "-")
        is_valid = BirthdayHandler.birthday_is_valid(birthday)

        if not is_valid:
            return BirthdayHandler.MSG_WRONG_FORMAT

        data = {
            "discord_id": f"{member_id}",
            "birthday": birthday
        }

        async with aiohttp.ClientSession(
            headers={
                "User-Agent": "Mozilla/5.0 (DiscordBot)",
                "Content-Type": "application/json",
                "Accept": "application/json",
            }
        ) as session:
            async with session.post(
                BirthdayHandler.WEBSITE_URL, json=data,
            ) as response:
                if response.status == 200:
                    return BirthdayHandler.MSG_ALL_OKAY
                return f"Erreur : {response.status}. {BirthdayHandler.MSG_BAD_ANSWER}"

    def birthday_is_valid(birthday: str) -> bool:
        try:
            query_date = datetime.strptime(birthday, '%Y-%m-%d').date()
        except Exception as e:
            return False

        return True