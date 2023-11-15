import sqlalchemy as db

engine = db.create_engine('sqlite:///mydb.sqlite')

con = engine.connect()

meta = db.MetaData()

Disc = db.Table (
    'Disc',
    meta,
    db.Column('name',db.String,primary_key=True),
    db.Column('manu',db.String,nullable=False),
    db.Column('speed',db.Integer,nullable=False)
)

meta.create_all(engine)

stmt = Disc.select().where(Disc.c.name == "Luna")
result = con.execute(stmt)
for r in result:
    print(r)