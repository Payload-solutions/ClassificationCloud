
from operator import index
from app import db
import pandas as pd


class YogurtData(db.Model):
    __tablename__ = "yogurt_features"
    features_id = db.Column(db.Integer, primary_key=True)
    streptococcus_initial = db.Column(db.Float, index=True, nullable=False)
    lactobacillus_initial = db.Column(db.Float, index=True, nullable=False)
    ideal_temperature = db.Column(db.Float, index=True, nullable=False)
    minimum_milk_proteins = db.Column(db.Float, index=True, nullable=False)
    titratable_acidity = db.Column(db.Float, index=True, nullable=False)
    ph_milk_sour = db.Column(db.Float, index=True, nullable=False)
    fat_milk_over_100mg = db.Column(db.Float, index=True, nullable=False)
    quality_product = db.Column(db.String(20), index=True, nullable=False)
    streptococcus_final = db.Column(db.Float, index=True, nullable=False)
    lactobacillus_final = db.Column(db.Float, index=True, nullable=False)
    quality_product_category = db.Column(db.Integer, index=True, nullable=False)

db.create_all()


def model_exists() -> bool:
    if not db.Query("yogurt_features").first():
        dataframe = pd.read_csv("classification_data.csv")
        dataframe.to_sql(name = "yogurt_features", con=db.engine, index=False)
model_exists()