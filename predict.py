import os
import pickle
import sys, os
sys.path.append('D:/Downloads/Fashion_Analysis/Fashion_Analysis/detectron2')
sys.path.append('D:/Downloads/Fashion_Analysis/Fashion_Analysis/detectron2/detectron2')
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
from detectron2.engine import DefaultPredictor
from detectron2.data import MetadataCatalog

from utils import *


main_dir = os.path.dirname(os.path.realpath(__file__))
data_dir = os.path.join(main_dir,"data") # Tahmin edilecek resimin bulunduğu klasör
save_dir = os.path.join(main_dir,"results") # Tahmin sonuçlarının kaydedileceği klasör
models_dir = os.path.join(main_dir,"modeller") # Model dosyalarının bulunduğu klasör

cfg_path = os.path.join(models_dir, "SE_CFG_3.pickle") # Modelin pickle dosyasının ismi
model_path = os.path.join(models_dir, "model_final.pth") # Model dosyasının ismi

cfg = get_cfg(cfg_path,model_path)
predictor = DefaultPredictor(cfg)

def main():
    dosya_ismi = sys.argv[1]
    image_path = os.path.join(data_dir, dosya_ismi) # Tahmin edilecek resmin ismi
    predict_image(image_path, predictor, cfg,save_dir=save_dir, show=True)

if __name__ == '__main__':
    main()
