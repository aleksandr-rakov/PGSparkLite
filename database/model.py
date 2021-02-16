import json

from peewee import (BooleanField, CharField, ForeignKeyField, IntegerField,
                    Model, SqliteDatabase)

database = SqliteDatabase('pgsparklite.db')


class BaseModel(Model):
    id = IntegerField(primary_key=True, unique=True)

    class Meta:
        database = database


class PedalParameter(BaseModel):
    effect_name = CharField()
    on_off = CharField()
    _parameters = CharField()

    def parameters(self):
        return json.loads(self._parameters)

    def store_parameters(self, parameters):
        self._parameters = json.dumps(parameters)


class PedalPreset(BaseModel):
    name = CharField()
    pedal_parameter = ForeignKeyField(PedalParameter)
    effect_name = CharField(index=True)
    visible = BooleanField(default=True)


class ChainPreset(BaseModel):
    name = CharField()
    uuid = CharField()
    bpm = IntegerField(default=120)
    system_preset_id = IntegerField(null=True, unique=True)
    gate_pedal = ForeignKeyField(PedalParameter)
    comp_pedal = ForeignKeyField(PedalParameter)
    drive_pedal = ForeignKeyField(PedalParameter)
    amp_pedal = ForeignKeyField(PedalParameter)
    mod_pedal = ForeignKeyField(PedalParameter)
    delay_pedal = ForeignKeyField(PedalParameter)
    reverb_pedal = ForeignKeyField(PedalParameter)


# Create and initialise the database if necessary
database.create_tables([PedalParameter, PedalPreset, ChainPreset])
