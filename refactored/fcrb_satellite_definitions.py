from sqlalchemy import Column, String, Integer, DateTime 

fcrb_satellite_definitions = {
    "diagnostic": {
        "lfdnr": Column("lfdnr", String(3)),
        "dkey1": Column("dkey1", String(30)),
        "erdat": Column("erdat", DateTime(timezone=False)),
        "begdt": Column("begdt", DateTime(timezone=False)),
        "enddt": Column("enddt",DateTime(timezone=False))
    },
    "episode": {
        "erdat": Column("erdat", DateTime(timezone=False)),
        "begdt": Column("begdt",DateTime(timezone=False)),
        "enddt": Column("enddt",DateTime(timezone=False)),
        "falar": Column("falar",String(1)),
        "bekat": Column("bekat",String(40)),
        "einzg": Column("einzg",String(9)),
        "statu": Column("statu",String(1)),
        "krzan": Column("krzan",String(1)),
        "storn": Column("storn",String(1)),
        "casetx": Column("casetx",String(20)),
        "fatxt": Column("fatxt",String(40)),
        "enddtx": Column("enddtx",String(20))
    }

}