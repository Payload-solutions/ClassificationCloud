
from app import db
import pandas as pd


class YogurtData(db.Model):
    __tablename__ = "features_data"
    index = db.Column(db.Integer, primary_key=True)
    streptococcus_initial_strain_cfu_ml = db.Column(db.Float, index=True, nullable=False)
    lactobacillus_initial_strain_cfu_ml = db.Column(db.Float, index=True, nullable=False)
    ideal_temperature_c = db.Column(db.Float, index=True, nullable=False)
    minimum_milk_proteins = db.Column(db.Float, index=True, nullable=False)
    titratable_acidity = db.Column(db.Float, index=True, nullable=False)
    pH_milk_sour_ = db.Column(db.Float, index=True, nullable=False)
    fat_milk_over_100mg_ = db.Column(db.Float, index=True, nullable=False)
    quality_product = db.Column(db.String(20), index=True, nullable=False)
    lactobacillus_final_cfu_ml = db.Column(db.Float, index=True, nullable=False)
    streptococcus_final_cfu_ml = db.Column(db.Float, index=True, nullable=False)
    quality_product_ = db.Column(db.Integer, index=True, nullable=False)


    def __init__(self, index: int,
                streptococcus_initial_strain_cfu_ml: float,
                lactobacillus_initial_strain_cfu_ml: float,
                ideal_temperature_c: float,
                minimum_milk_proteins: float,
                titratable_acidity: float,
                pH_milk_sour_: float,
                fat_milk_over_100mg_: float,
                quality_product: str,
                lactobacillus_final_cfu_ml: float,
                streptococcus_final_cfu_ml: float,
                quality_product_) -> None:

        self.index  =       index
        self.streptococcus_initial_strain_cfu_ml  = streptococcus_initial_strain_cfu_ml
        self.lactobacillus_initial_strain_cfu_ml  = lactobacillus_initial_strain_cfu_ml
        self.ideal_temperature_c  = ideal_temperature_c
        self.minimum_milk_proteins  = minimum_milk_proteins
        self.titratable_acidity  = titratable_acidity
        self.pH_milk_sour_  = pH_milk_sour_
        self.fat_milk_over_100mg_  = fat_milk_over_100mg_
        self.quality_product  = quality_product
        self.lactobacillus_final_cfu_ml  = lactobacillus_final_cfu_ml
        self.streptococcus_final_cfu_ml  = streptococcus_final_cfu_ml
        self.quality_product_  = quality_product_
         

db.create_all()
dataframe = pd.read_csv("app/classification_data.csv")
dataframe.to_sql(name = "features_data", if_exists="replace", con=db.engine, index=True)

