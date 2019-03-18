from sqlalchemy.orm import sessionmaker
from models.player import Player
from models.player_inventory import PlayerInventory
from common.database import db_engine


def initialize_player(name, id):
    session_maker = sessionmaker(bind=db_engine)
    session = session_maker()
    player = session.query(Player).filter(Player.id == id).first()
    if not player:
        new_player = Player(id=id, name=name)
        session.add(new_player)
        session.commit()
