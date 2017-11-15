from extranet import db


class Base(db.Model):

    __abstract__ = True
    __table_args__ = {
        'mysql_row_format': 'DYNAMIC'
    }

    # id
    id = db.Column(db.Integer, primary_key=True)


class Dated(Base):

    __abstract__ = True

    # timestamps
    ctime = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    mtime = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp(),
                      onupdate=db.func.current_timestamp())


class Intra(Base):

    __abstract__ = True

    # crawler timestamps
    # itime = first indexation time
    # utime = last update time
    itime = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    utime = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp(),
                      onupdate=db.func.current_timestamp())
