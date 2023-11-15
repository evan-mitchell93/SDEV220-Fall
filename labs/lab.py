import sqlalchemy as db

engine = db.create_engine('sqlite:///mydb.sqlite',echo=True)
connection = engine.connect()
meta = db.MetaData()

Disc = db.Table(
    'Disc', 
    meta,
    db.Column('name',db.String,primary_key=True),
    db.Column('manu',db.String,nullable=False),
    db.Column('speed',db.Integer,nullable=False),
    db.Column('glide',db.Integer,nullable=False)

)

meta.create_all(engine)


results = connection.execute(Disc.select())
discs = []
for disc in results:
    discs.append(disc)

print(discs)