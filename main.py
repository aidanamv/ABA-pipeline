import json
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import statsmodels
import statsmodels.api as sm
from statsmodels.formula.api import ols
import glob
import csv
from scipy.stats import ttest_ind
from statannot import add_stat_annotation
#extracting data from specified folders
folders=glob.glob("/home/healthineer/PycharmProject/tau_project/venv/ABA-pipeline/*/*")
num_elements=len(folders)
group_names={};
file_paths={};
print(num_elements)
for i in range(num_elements):
	file_paths[i]=folders[i]
	group_name =folders[i].replace("/home/healthineer/PycharmProject/tau_project/venv/ABA-pipeline/","").replace("/*", "")
	index=group_name.find("/");
	group_names[i]=group_name[0:index];

print(group_names)
print(file_paths[1])
subiculum_list={};
corpus_callosum_list={};
cerebal_peduncle_list={};
internal_capsule_list={};
anterior_commissure_list={};
thalamus={};
hippocampus={};
cortex={};
for i in range(num_elements):
    with open(file_paths[i]) as json_file:
        data = json.load(json_file)
        subiculum_list[i]=data["/P56_atlas"]["wdti_rD"]["Subiculum"];
        corpus_callosum_list[i]=(data["/P56_atlas"]["wdti_rD"]["corpus_callosum,_body"]
        +data["/P56_atlas"]["wdti_rD"]["corpus_callosum,_splenium"]
        +data["/P56_atlas"]["wdti_rD"]["genu_of_corpus_callosum"])/3
        cerebal_peduncle_list[i]=data["/P56_atlas"]["wdti_rD"]["cerebal_peduncle"];
        internal_capsule_list[i]=data["/P56_atlas"]["wdti_rD"]["internal_capsule"];
        anterior_commissure_list[i]=(data["/P56_atlas"]["wdti_rD"]["anterior_commissure,_olfactory_limb"]
        +data["/P56_atlas"]["wdti_rD"]["anterior_commissure,_temporal_limb"])/2
        thalamus[i]=data["/P56_atlas"]["wdti_rD"]["Thalamus"];
        hippocampus[i]=data["/P56_atlas"]["wdti_rD"]["Dentate_gyrus,_granule_cell_layer"]
        +data["/P56_atlas"]["wdti_rD"]["Dentate_gyrus,_molecular_layer"]
        +data["/P56_atlas"]["wdti_rD"]["Dentate_gyrus,_polymorph_layer"]
        +data["/P56_atlas"]["wdti_rD"]["Field_CA1"]
        +data["/P56_atlas"]["wdti_rD"]["Field_CA2"]
        +data["/P56_atlas"]["wdti_rD"]["Field_CA3"]
        +data["/P56_atlas"]["wdti_rD"]["Fasciola_cinerea"]
        cortex[i]=(data["/P56_atlas"]["wdti_rD"]["Frontal_pole,_layer_1"]
        +data["/P56_atlas"]["wdti_rD"]["Frontal_pole,_layer_2/3"]
        +data["/P56_atlas"]["wdti_rD"]["Frontal_pole,_layer_5"]
        +data["/P56_atlas"]["wdti_rD"]["Frontal_pole,_layer_6a"]
        +data["/P56_atlas"]["wdti_rD"]["Primary_motor_area,_Layer_1"]
        +data["/P56_atlas"]["wdti_rD"]["Primary_motor_area,_Layer_2/3"]
        +data["/P56_atlas"]["wdti_rD"]["Primary_motor_area,_Layer_5"]
        +data["/P56_atlas"]["wdti_rD"]["Primary_motor_area,_Layer_6a"]
        +data["/P56_atlas"]["wdti_rD"]["Primary_motor_area,_Layer_6b"]
        +data["/P56_atlas"]["wdti_rD"]["Secondary_motor_area,_layer_1"]
        +data["/P56_atlas"]["wdti_rD"]["Secondary_motor_area,_layer_2/3"]
        +data["/P56_atlas"]["wdti_rD"]["Secondary_motor_area,_layer_5"]
        +data["/P56_atlas"]["wdti_rD"]["Secondary_motor_area,_layer_6a"]
        +data["/P56_atlas"]["wdti_rD"]["Secondary_motor_area,_layer_6b"]
        +data["/P56_atlas"]["wdti_rD"]["Primary_somatosensory_area,_nose,_layer_1"]
        +data["/P56_atlas"]["wdti_rD"]["Primary_somatosensory_area,_nose,_layer_2/3"]
        +data["/P56_atlas"]["wdti_rD"]["Primary_somatosensory_area,_nose,_layer_4"]
        +data["/P56_atlas"]["wdti_rD"]["Primary_somatosensory_area,_nose,_layer_5"]
        +data["/P56_atlas"]["wdti_rD"]["Primary_somatosensory_area,_nose,_layer_6a"]
        +data["/P56_atlas"]["wdti_rD"]["Primary_somatosensory_area,_nose,_layer_6b"]
        +data["/P56_atlas"]["wdti_rD"]["Primary_somatosensory_area,_barrel_field,_layer_1"]
        +data["/P56_atlas"]["wdti_rD"]["Primary_somatosensory_area,_barrel_field,_layer_2/3"]
        +data["/P56_atlas"]["wdti_rD"]["Primary_somatosensory_area,_barrel_field,_layer_4"]
        +data["/P56_atlas"]["wdti_rD"]["Primary_somatosensory_area,_barrel_field,_layer_5"]
        +data["/P56_atlas"]["wdti_rD"]["Primary_somatosensory_area,_barrel_field,_layer_6a"]
        +data["/P56_atlas"]["wdti_rD"]["Primary_somatosensory_area,_barrel_field,_layer_6b"]
        +data["/P56_atlas"]["wdti_rD"]["Primary_somatosensory_area,_lower_limb,_layer_1"]
        +data["/P56_atlas"]["wdti_rD"]["Primary_somatosensory_area,_lower_limb,_layer_2/3"]
        +data["/P56_atlas"]["wdti_rD"]["Primary_somatosensory_area,_lower_limb,_layer_4"]
        +data["/P56_atlas"]["wdti_rD"]["Primary_somatosensory_area,_lower_limb,_layer_5"]
        +data["/P56_atlas"]["wdti_rD"]["Primary_somatosensory_area,_lower_limb,_layer_6a"]
        +data["/P56_atlas"]["wdti_rD"]["Primary_somatosensory_area,_lower_limb,_layer_6b"]
        +data["/P56_atlas"]["wdti_rD"]["Primary_somatosensory_area,_mouth,_layer_1"]
        +data["/P56_atlas"]["wdti_rD"]["Primary_somatosensory_area,_mouth,_layer_2/3"]
        +data["/P56_atlas"]["wdti_rD"]["Primary_somatosensory_area,_mouth,_layer_4"]
        +data["/P56_atlas"]["wdti_rD"]["Primary_somatosensory_area,_mouth,_layer_5"]
        +data["/P56_atlas"]["wdti_rD"]["Primary_somatosensory_area,_mouth,_layer_6a"]
        +data["/P56_atlas"]["wdti_rD"]["Primary_somatosensory_area,_mouth,_layer_6b"]
        +data["/P56_atlas"]["wdti_rD"]["Primary_somatosensory_area,_upper_limb,_layer_1"]
        +data["/P56_atlas"]["wdti_rD"]["Primary_somatosensory_area,_upper_limb,_layer_2/3"]
        +data["/P56_atlas"]["wdti_rD"]["Primary_somatosensory_area,_upper_limb,_layer_4"]
        +data["/P56_atlas"]["wdti_rD"]["Primary_somatosensory_area,_upper_limb,_layer_5"]
        +data["/P56_atlas"]["wdti_rD"]["Primary_somatosensory_area,_upper_limb,_layer_6a"]
        +data["/P56_atlas"]["wdti_rD"]["Primary_somatosensory_area,_upper_limb,_layer_6b"]
        +data["/P56_atlas"]["wdti_rD"]["Primary_somatosensory_area,_trunk,_layer_1"]
        +data["/P56_atlas"]["wdti_rD"]["Primary_somatosensory_area,_trunk,_layer_2/3"]
        +data["/P56_atlas"]["wdti_rD"]["Primary_somatosensory_area,_trunk,_layer_4"]
        +data["/P56_atlas"]["wdti_rD"]["Primary_somatosensory_area,_trunk,_layer_5"]
        +data["/P56_atlas"]["wdti_rD"]["Primary_somatosensory_area,_trunk,_layer_6a"]
        +data["/P56_atlas"]["wdti_rD"]["Primary_somatosensory_area,_trunk,_layer_6b"]
        +data["/P56_atlas"]["wdti_rD"]["Primary_somatosensory_area,_unassigned,_layer_1"]
        +data["/P56_atlas"]["wdti_rD"]["Primary_somatosensory_area,_unassigned,_layer_2/3"]
        +data["/P56_atlas"]["wdti_rD"]["Primary_somatosensory_area,_unassigned,_layer_4"]
        +data["/P56_atlas"]["wdti_rD"]["Primary_somatosensory_area,_unassigned,_layer_5"]
        +data["/P56_atlas"]["wdti_rD"]["Primary_somatosensory_area,_unassigned,_layer_6a"]
        +data["/P56_atlas"]["wdti_rD"]["Primary_somatosensory_area,_unassigned,_layer_6b"]
        +data["/P56_atlas"]["wdti_rD"]["Supplemental_somatosensory_area,_layer_1"]
        +data["/P56_atlas"]["wdti_rD"]["Supplemental_somatosensory_area,_layer_2/3"]
        +data["/P56_atlas"]["wdti_rD"]["Supplemental_somatosensory_area,_layer_4"]
        +data["/P56_atlas"]["wdti_rD"]["Supplemental_somatosensory_area,_layer_5"]
        +data["/P56_atlas"]["wdti_rD"]["Supplemental_somatosensory_area,_layer_6a"]
        +data["/P56_atlas"]["wdti_rD"]["Supplemental_somatosensory_area,_layer_6b"]
        +data["/P56_atlas"]["wdti_rD"]["Gustatory_areas,_layer_1"]
        +data["/P56_atlas"]["wdti_rD"]["Gustatory_areas,_layer_2/3"]
        +data["/P56_atlas"]["wdti_rD"]["Gustatory_areas,_layer_4"]
        +data["/P56_atlas"]["wdti_rD"]["Gustatory_areas,_layer_5"]
        +data["/P56_atlas"]["wdti_rD"]["Gustatory_areas,_layer_6a"]
        +data["/P56_atlas"]["wdti_rD"]["Gustatory_areas,_layer_6b"]
        +data["/P56_atlas"]["wdti_rD"]["Visceral_area,_layer_1"]
        +data["/P56_atlas"]["wdti_rD"]["Visceral_area,_layer_2/3"]
        +data["/P56_atlas"]["wdti_rD"]["Visceral_area,_layer_4"]
        +data["/P56_atlas"]["wdti_rD"]["Visceral_area,_layer_5"]
        +data["/P56_atlas"]["wdti_rD"]["Visceral_area,_layer_6a"]
        +data["/P56_atlas"]["wdti_rD"]["Visceral_area,_layer_6b"]
        +data["/P56_atlas"]["wdti_rD"]["Dorsal_auditory_area,_layer_1"]
        +data["/P56_atlas"]["wdti_rD"]["Dorsal_auditory_area,_layer_2/3"]
        +data["/P56_atlas"]["wdti_rD"]["Dorsal_auditory_area,_layer_4"]
        +data["/P56_atlas"]["wdti_rD"]["Dorsal_auditory_area,_layer_5"]
        +data["/P56_atlas"]["wdti_rD"]["Dorsal_auditory_area,_layer_6a"]
        +data["/P56_atlas"]["wdti_rD"]["Dorsal_auditory_area,_layer_6b"]
        +data["/P56_atlas"]["wdti_rD"]["Primary_auditory_area,_layer_1"]
        +data["/P56_atlas"]["wdti_rD"]["Primary_auditory_area,_layer_2/3"]
        +data["/P56_atlas"]["wdti_rD"]["Primary_auditory_area,_layer_4"]
        +data["/P56_atlas"]["wdti_rD"]["Primary_auditory_area,_layer_5"]
        +data["/P56_atlas"]["wdti_rD"]["Primary_auditory_area,_layer_6a"]
        +data["/P56_atlas"]["wdti_rD"]["Primary_auditory_area,_layer_6b"]
        +data["/P56_atlas"]["wdti_rD"]["Posterior_auditory_area,_layer_1"]
        +data["/P56_atlas"]["wdti_rD"]["Posterior_auditory_area,_layer_2/3"]
        +data["/P56_atlas"]["wdti_rD"]["Posterior_auditory_area,_layer_4"]
        +data["/P56_atlas"]["wdti_rD"]["Posterior_auditory_area,_layer_5"]
        +data["/P56_atlas"]["wdti_rD"]["Posterior_auditory_area,_layer_6a"]
        +data["/P56_atlas"]["wdti_rD"]["Posterior_auditory_area,_layer_6b"]
        +data["/P56_atlas"]["wdti_rD"]["Ventral_auditory_area,_layer_1"]
        +data["/P56_atlas"]["wdti_rD"]["Ventral_auditory_area,_layer_2/3"]
        +data["/P56_atlas"]["wdti_rD"]["Ventral_auditory_area,_layer_4"]
        +data["/P56_atlas"]["wdti_rD"]["Ventral_auditory_area,_layer_5"]
        +data["/P56_atlas"]["wdti_rD"]["Ventral_auditory_area,_layer_6a"]
        +data["/P56_atlas"]["wdti_rD"]["Ventral_auditory_area,_layer_6b"]
        +data["/P56_atlas"]["wdti_rD"]["Anterolateral_visual_area,_layer_1"]
        +data["/P56_atlas"]["wdti_rD"]["Anterolateral_visual_area,_layer_2/3"]
        +data["/P56_atlas"]["wdti_rD"]["Anterolateral_visual_area,_layer_4"]
        +data["/P56_atlas"]["wdti_rD"]["Anterolateral_visual_area,_layer_5"]
        +data["/P56_atlas"]["wdti_rD"]["Anterolateral_visual_area,_layer_6a"]
        +data["/P56_atlas"]["wdti_rD"]["Anterolateral_visual_area,_layer_6b"]
        +data["/P56_atlas"]["wdti_rD"]["Anteromedial_visual_area,_layer_1"]
        +data["/P56_atlas"]["wdti_rD"]["Anteromedial_visual_area,_layer_2/3"]
        +data["/P56_atlas"]["wdti_rD"]["Anteromedial_visual_area,_layer_4"]
        +data["/P56_atlas"]["wdti_rD"]["Anteromedial_visual_area,_layer_5"]
        +data["/P56_atlas"]["wdti_rD"]["Anteromedial_visual_area,_layer_6a"]
        +data["/P56_atlas"]["wdti_rD"]["Anteromedial_visual_area,_layer_6b"]
        +data["/P56_atlas"]["wdti_rD"]["Lateral_visual_area,_layer_1"]
        +data["/P56_atlas"]["wdti_rD"]["Lateral_visual_area,_layer_2/3"]
        +data["/P56_atlas"]["wdti_rD"]["Lateral_visual_area,_layer_4"]
        +data["/P56_atlas"]["wdti_rD"]["Lateral_visual_area,_layer_5"]
        +data["/P56_atlas"]["wdti_rD"]["Lateral_visual_area,_layer_6a"]
        +data["/P56_atlas"]["wdti_rD"]["Lateral_visual_area,_layer_6b"]
        +data["/P56_atlas"]["wdti_rD"]["Primary_visual_area,_layer_1"]
        +data["/P56_atlas"]["wdti_rD"]["Primary_visual_area,_layer_2/3"]
        +data["/P56_atlas"]["wdti_rD"]["Primary_visual_area,_layer_4"]
        +data["/P56_atlas"]["wdti_rD"]["Primary_visual_area,_layer_5"]
        +data["/P56_atlas"]["wdti_rD"]["Primary_visual_area,_layer_6a"]
        +data["/P56_atlas"]["wdti_rD"]["Primary_visual_area,_layer_6b"]
        +data["/P56_atlas"]["wdti_rD"]["Posterolateral_visual_area,_layer_1"]
        +data["/P56_atlas"]["wdti_rD"]["Posterolateral_visual_area,_layer_2/3"]
        +data["/P56_atlas"]["wdti_rD"]["Posterolateral_visual_area,_layer_4"]
        +data["/P56_atlas"]["wdti_rD"]["Posterolateral_visual_area,_layer_5"]
        +data["/P56_atlas"]["wdti_rD"]["Posterolateral_visual_area,_layer_6a"]
        +data["/P56_atlas"]["wdti_rD"]["Posterolateral_visual_area,_layer_6b"]
        +data["/P56_atlas"]["wdti_rD"]["posteromedial_visual_area,_layer_1"]
        +data["/P56_atlas"]["wdti_rD"]["posteromedial_visual_area,_layer_2/3"]
        +data["/P56_atlas"]["wdti_rD"]["posteromedial_visual_area,_layer_4"]
        +data["/P56_atlas"]["wdti_rD"]["posteromedial_visual_area,_layer_5"]
        +data["/P56_atlas"]["wdti_rD"]["posteromedial_visual_area,_layer_6a"]
        +data["/P56_atlas"]["wdti_rD"]["posteromedial_visual_area,_layer_6b"]
        +data["/P56_atlas"]["wdti_rD"]["Anterior_cingulate_area,_dorsal_part,_layer_1"]
        +data["/P56_atlas"]["wdti_rD"]["Anterior_cingulate_area,_dorsal_part,_layer_2/3"]
        +data["/P56_atlas"]["wdti_rD"]["Anterior_cingulate_area,_dorsal_part,_layer_5"]
        +data["/P56_atlas"]["wdti_rD"]["Anterior_cingulate_area,_dorsal_part,_layer_6a"]
        +data["/P56_atlas"]["wdti_rD"]["Anterior_cingulate_area,_dorsal_part,_layer_6b"]
        +data["/P56_atlas"]["wdti_rD"]["Anterior_cingulate_area,_ventral_part,_layer_1"]
        +data["/P56_atlas"]["wdti_rD"]["Anterior_cingulate_area,_ventral_part,_layer_2/3"]
        +data["/P56_atlas"]["wdti_rD"]["Anterior_cingulate_area,_ventral_part,_layer_5"]
        +data["/P56_atlas"]["wdti_rD"]["Anterior_cingulate_area,_ventral_part,_6a"]
        +data["/P56_atlas"]["wdti_rD"]["Anterior_cingulate_area,_ventral_part,_6b"]
        +data["/P56_atlas"]["wdti_rD"]["Prelimbic_area,_layer_1"]
        +data["/P56_atlas"]["wdti_rD"]["Prelimbic_area,_layer_2/3"]
        +data["/P56_atlas"]["wdti_rD"]["Prelimbic_area,_layer_5"]
        +data["/P56_atlas"]["wdti_rD"]["Prelimbic_area,_layer_6a"]
        +data["/P56_atlas"]["wdti_rD"]["Prelimbic_area,_layer_6b"]
        +data["/P56_atlas"]["wdti_rD"]["Infralimbic_area,_layer_1"]
        +data["/P56_atlas"]["wdti_rD"]["Infralimbic_area,_layer_2/3"]
        +data["/P56_atlas"]["wdti_rD"]["Infralimbic_area,_layer_5"]
        +data["/P56_atlas"]["wdti_rD"]["Infralimbic_area,_layer_6a"]
        +data["/P56_atlas"]["wdti_rD"]["Infralimbic_area,_layer_6b"]
        +data["/P56_atlas"]["wdti_rD"]["Orbital_area,_lateral_part,_layer_1"]
        +data["/P56_atlas"]["wdti_rD"]["Orbital_area,_lateral_part,_layer_2/3"]
        +data["/P56_atlas"]["wdti_rD"]["Orbital_area,_lateral_part,_layer_5"]
        +data["/P56_atlas"]["wdti_rD"]["Orbital_area,_lateral_part,_layer_6a"]
        +data["/P56_atlas"]["wdti_rD"]["Orbital_area,_lateral_part,_layer_6b"]
        +data["/P56_atlas"]["wdti_rD"]["Orbital_area,_medial_part,_layer_1"]
        +data["/P56_atlas"]["wdti_rD"]["Orbital_area,_medial_part,_layer_2/3"]
        +data["/P56_atlas"]["wdti_rD"]["Orbital_area,_medial_part,_layer_5"]
        +data["/P56_atlas"]["wdti_rD"]["Orbital_area,_medial_part,_layer_6a"]
        +data["/P56_atlas"]["wdti_rD"]["Orbital_area,_medial_part,_layer_6b"]
        +data["/P56_atlas"]["wdti_rD"]["Orbital_area,_ventrolateral_part,_layer_1"]
        +data["/P56_atlas"]["wdti_rD"]["Orbital_area,_ventrolateral_part,_layer_2/3"]
        +data["/P56_atlas"]["wdti_rD"]["Orbital_area,_ventrolateral_part,_layer_5"]
        +data["/P56_atlas"]["wdti_rD"]["Orbital_area,_ventrolateral_part,_layer_6a"]
        +data["/P56_atlas"]["wdti_rD"]["Orbital_area,_ventrolateral_part,_layer_6b"]
        +data["/P56_atlas"]["wdti_rD"]["Agranular_insular_area,_dorsal_part,_layer_1"]
        +data["/P56_atlas"]["wdti_rD"]["Agranular_insular_area,_dorsal_part,_layer_2/3"]
        +data["/P56_atlas"]["wdti_rD"]["Agranular_insular_area,_dorsal_part,_layer_5"]
        +data["/P56_atlas"]["wdti_rD"]["Agranular_insular_area,_dorsal_part,_layer_6a"]
        +data["/P56_atlas"]["wdti_rD"]["Agranular_insular_area,_dorsal_part,_layer_6b"]
        +data["/P56_atlas"]["wdti_rD"]["Agranular_insular_area,_posterior_part,_layer_1"]
        +data["/P56_atlas"]["wdti_rD"]["Agranular_insular_area,_posterior_part,_layer_2/3"]
        +data["/P56_atlas"]["wdti_rD"]["Agranular_insular_area,_posterior_part,_layer_5"]
        +data["/P56_atlas"]["wdti_rD"]["Agranular_insular_area,_posterior_part,_layer_6a"]
        +data["/P56_atlas"]["wdti_rD"]["Agranular_insular_area,_posterior_part,_layer_6b"]
        +data["/P56_atlas"]["wdti_rD"]["Agranular_insular_area,_ventral_part,_layer_1"]
        +data["/P56_atlas"]["wdti_rD"]["Agranular_insular_area,_ventral_part,_layer_2/3"]
        +data["/P56_atlas"]["wdti_rD"]["Agranular_insular_area,_ventral_part,_layer_5"]
        +data["/P56_atlas"]["wdti_rD"]["Agranular_insular_area,_ventral_part,_layer_6a"]
        +data["/P56_atlas"]["wdti_rD"]["Agranular_insular_area,_ventral_part,_layer_6b"]
        +data["/P56_atlas"]["wdti_rD"]["Retrosplenial_area,_dorsal_part,_layer_1"]
        +data["/P56_atlas"]["wdti_rD"]["Retrosplenial_area,_dorsal_part,_layer_2/3"]
        +data["/P56_atlas"]["wdti_rD"]["Retrosplenial_area,_dorsal_part,_layer_5"]
        +data["/P56_atlas"]["wdti_rD"]["Retrosplenial_area,_dorsal_part,_layer_6a"]
        +data["/P56_atlas"]["wdti_rD"]["Retrosplenial_area,_dorsal_part,_layer_6b"]
        +data["/P56_atlas"]["wdti_rD"]["Retrosplenial_area,_lateral_agranular_part,_layer_1"]
        +data["/P56_atlas"]["wdti_rD"]["Retrosplenial_area,_lateral_agranular_part,_layer_2/3"]
        +data["/P56_atlas"]["wdti_rD"]["Retrosplenial_area,_lateral_agranular_part,_layer_5"]
        +data["/P56_atlas"]["wdti_rD"]["Retrosplenial_area,_lateral_agranular_part,_layer_6a"]
        +data["/P56_atlas"]["wdti_rD"]["Retrosplenial_area,_lateral_agranular_part,_layer_6b"]
        +data["/P56_atlas"]["wdti_rD"]["Retrosplenial_area,_ventral_part,_layer_1"]
        +data["/P56_atlas"]["wdti_rD"]["Retrosplenial_area,_ventral_part,_layer_2/3"]
        +data["/P56_atlas"]["wdti_rD"]["Retrosplenial_area,_ventral_part,_layer_5"]
        +data["/P56_atlas"]["wdti_rD"]["Retrosplenial_area,_ventral_part,_layer_6a"]
        +data["/P56_atlas"]["wdti_rD"]["Retrosplenial_area,_ventral_part,_layer_6b"]
        +data["/P56_atlas"]["wdti_rD"]["Temporal_association_areas,_layer_1"]
        +data["/P56_atlas"]["wdti_rD"]["Temporal_association_areas,_layer_2/3"]
        +data["/P56_atlas"]["wdti_rD"]["Temporal_association_areas,_layer_4"]
        +data["/P56_atlas"]["wdti_rD"]["Temporal_association_areas,_layer_5"]
        +data["/P56_atlas"]["wdti_rD"]["Temporal_association_areas,_layer_6a"]
        +data["/P56_atlas"]["wdti_rD"]["Temporal_association_areas,_layer_6b"]
        +data["/P56_atlas"]["wdti_rD"]["Perirhinal_area,_layer_1"]
        +data["/P56_atlas"]["wdti_rD"]["Perirhinal_area,_layer_2/3"]
        +data["/P56_atlas"]["wdti_rD"]["Perirhinal_area,_layer_5"]
        +data["/P56_atlas"]["wdti_rD"]["Perirhinal_area,_layer_6a"]
        +data["/P56_atlas"]["wdti_rD"]["Perirhinal_area,_layer_6b"]
        +data["/P56_atlas"]["wdti_rD"]["Ectorhinal_area/Layer_1"]
        +data["/P56_atlas"]["wdti_rD"]["Ectorhinal_area/Layer_2/3"]
        +data["/P56_atlas"]["wdti_rD"]["Ectorhinal_area/Layer_5"]
        +data["/P56_atlas"]["wdti_rD"]["Ectorhinal_area/Layer_6a"]
        +data["/P56_atlas"]["wdti_rD"]["Ectorhinal_area/Layer_6b"])/215;

# saving the data in csv file
with open("data_wdti_rD.csv", "w") as csvfile:
    filewriter = csv.writer(csvfile, delimiter=",",quotechar="|", quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(["Region","Group", "dti_rD"])
    for i in range(num_elements):
        filewriter.writerow(["SUB", group_names[i], subiculum_list[i]])
        filewriter.writerow(["CC", group_names[i], corpus_callosum_list[i]])
        filewriter.writerow(["CPD", group_names[i], cerebal_peduncle_list[i]])
        filewriter.writerow(["AC", group_names[i], anterior_commissure_list[i]])
        filewriter.writerow(["TH", group_names[i], thalamus[i]])
        filewriter.writerow(["HPR", group_names[i], hippocampus[i]])
        filewriter.writerow(["CRX", group_names[i], cortex[i]])


data = pd.read_csv("data_wdti_rD.csv")
data["Region"] = pd.Categorical(data["Region"])
data["Group"] = pd.Categorical(data["Group"])
#generating bar plot of mean values of each region
sns.set(font_scale=3,font='bold') #sets font size for chart scales
sns.set_style("white")
seq_col_brew = sns.color_palette("Greys", 3)
sns.set_palette(seq_col_brew)
#sns.set_palette(['#000000', '#ABABAB'])
ax=sns.boxplot(x="Region", y="dti_rD", hue="Group", data=data,hue_order=["non-transgene","heterozygote", "homozygote"])
ax = sns.swarmplot(x="Region", y="dti_rD", hue="Group",data=data,dodge=True,hue_order=["non-transgene","heterozygote", "homozygote"],color=".25")
ax.set_ylabel("RD", rotation =90 ) # y-axis label,
#ax.set_xticklabels(['AC$^a$','CC$^a$','CPD$^a$','CRX$^a$','HPR$^a$','SUB$^a$','TH$^a$'])
ax.set(xlabel=None)
group_nTG=data[data['Group']=='non-transgene']
group_nTG.groupby('Region')['dti_rD'].aggregate(['mean','std'])

group_homoo=data[data['Group']=='homozygote']
group_homoo.groupby('Region')['dti_rD'].aggregate(['mean','std'])

homo_CC=group_homoo[group_homoo['Region']=='AC']
ntg_CC=group_nTG[group_nTG['Region']=='AC']

print(ttest_ind(homo_CC['dti_rD'],ntg_CC['dti_rD']))
# Compute pvalues and
add_stat_annotation(ax, data=data, x="Region", y="dti_rD", hue="Group", hue_order=["non-transgene","heterozygote", "homozygote"],
                    box_pairs=[(("AC", "homozygote"), ("AC", "non-transgene")),
                            (("AC", "homozygote"), ("AC", "heterozygote")),
                                 (("CC", "homozygote"), ("CC", "non-transgene")),
                                 (("CC", "homozygote"), ("CC", "heterozygote")),
                               (("CRX", "homozygote"), ("CRX", "heterozygote")),
                               (("CRX", "homozygote"), ("CRX", "non-transgene")),
                               (("CPD", "homozygote"), ("CPD", "heterozygote")),
                             # (("CPD", "homozygote"), ("CPD", "non-transgene")),
                                (("HPR", "homozygote"), ("HPR", "heterozygote")),
                               (("HPR", "homozygote"), ("HPR", "non-transgene")),
                               (("SUB", "homozygote"), ("SUB", "heterozygote")),
                               (("SUB", "homozygote"), ("SUB", "non-transgene")),
                               (("TH", "homozygote"), ("TH", "heterozygote")),
                               (("TH", "homozygote"), ("TH", "non-transgene"))
                               ],
                    test='t-test_ind', text_format='star', comparisons_correction=None, loc='inside', verbose=2)
#plt.legend(loc='upper left', bbox_to_anchor=(1.03, 1))
#sns.despine(left=True, right=True)
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles=handles[0:3], labels=labels[0:3])#ax.set(ylim=(0, 0.7))
#ax.grid(False)
plt.savefig('RD.png')
plt.show()

#generating list of ROIs
subiculum_list={};
corpus_callosum_list={};
cerebal_peduncle_list={};
internal_capsule_list={};
anterior_commissure_list={};
thalamus={};
hippocampus={};
cortex={};
for i in range(num_elements):
    with open(file_paths[i]) as json_file:
        data = json.load(json_file)
        subiculum_list[i]=data["/P56_atlas"]["wdti_mD"]["Subiculum"];
        corpus_callosum_list[i]=(data["/P56_atlas"]["wdti_mD"]["corpus_callosum,_body"]
        +data["/P56_atlas"]["wdti_mD"]["corpus_callosum,_splenium"]
        +data["/P56_atlas"]["wdti_mD"]["genu_of_corpus_callosum"])/3
        cerebal_peduncle_list[i]=data["/P56_atlas"]["wdti_mD"]["cerebal_peduncle"];
        internal_capsule_list[i]=data["/P56_atlas"]["wdti_mD"]["internal_capsule"];
        anterior_commissure_list[i]=(data["/P56_atlas"]["wdti_mD"]["anterior_commissure,_olfactory_limb"]
        +data["/P56_atlas"]["wdti_mD"]["anterior_commissure,_temporal_limb"])/2
        thalamus[i]=data["/P56_atlas"]["wdti_mD"]["Thalamus"];
        hippocampus[i]=data["/P56_atlas"]["wdti_mD"]["Dentate_gyrus,_granule_cell_layer"]
        +data["/P56_atlas"]["wdti_mD"]["Dentate_gyrus,_molecular_layer"]
        +data["/P56_atlas"]["wdti_mD"]["Dentate_gyrus,_polymorph_layer"]
        +data["/P56_atlas"]["wdti_mD"]["Field_CA1"]
        +data["/P56_atlas"]["wdti_mD"]["Field_CA2"]
        +data["/P56_atlas"]["wdti_mD"]["Field_CA3"]
        +data["/P56_atlas"]["wdti_mD"]["Fasciola_cinerea"]
        cortex[i]=(data["/P56_atlas"]["wdti_mD"]["Frontal_pole,_layer_1"]
        +data["/P56_atlas"]["wdti_mD"]["Frontal_pole,_layer_2/3"]
        +data["/P56_atlas"]["wdti_mD"]["Frontal_pole,_layer_5"]
        +data["/P56_atlas"]["wdti_mD"]["Frontal_pole,_layer_6a"]
        +data["/P56_atlas"]["wdti_mD"]["Primary_motor_area,_Layer_1"]
        +data["/P56_atlas"]["wdti_mD"]["Primary_motor_area,_Layer_2/3"]
        +data["/P56_atlas"]["wdti_mD"]["Primary_motor_area,_Layer_5"]
        +data["/P56_atlas"]["wdti_mD"]["Primary_motor_area,_Layer_6a"]
        +data["/P56_atlas"]["wdti_mD"]["Primary_motor_area,_Layer_6b"]
        +data["/P56_atlas"]["wdti_mD"]["Secondary_motor_area,_layer_1"]
        +data["/P56_atlas"]["wdti_mD"]["Secondary_motor_area,_layer_2/3"]
        +data["/P56_atlas"]["wdti_mD"]["Secondary_motor_area,_layer_5"]
        +data["/P56_atlas"]["wdti_mD"]["Secondary_motor_area,_layer_6a"]
        +data["/P56_atlas"]["wdti_mD"]["Secondary_motor_area,_layer_6b"]
        +data["/P56_atlas"]["wdti_mD"]["Primary_somatosensory_area,_nose,_layer_1"]
        +data["/P56_atlas"]["wdti_mD"]["Primary_somatosensory_area,_nose,_layer_2/3"]
        +data["/P56_atlas"]["wdti_mD"]["Primary_somatosensory_area,_nose,_layer_4"]
        +data["/P56_atlas"]["wdti_mD"]["Primary_somatosensory_area,_nose,_layer_5"]
        +data["/P56_atlas"]["wdti_mD"]["Primary_somatosensory_area,_nose,_layer_6a"]
        +data["/P56_atlas"]["wdti_mD"]["Primary_somatosensory_area,_nose,_layer_6b"]
        +data["/P56_atlas"]["wdti_mD"]["Primary_somatosensory_area,_barrel_field,_layer_1"]
        +data["/P56_atlas"]["wdti_mD"]["Primary_somatosensory_area,_barrel_field,_layer_2/3"]
        +data["/P56_atlas"]["wdti_mD"]["Primary_somatosensory_area,_barrel_field,_layer_4"]
        +data["/P56_atlas"]["wdti_mD"]["Primary_somatosensory_area,_barrel_field,_layer_5"]
        +data["/P56_atlas"]["wdti_mD"]["Primary_somatosensory_area,_barrel_field,_layer_6a"]
        +data["/P56_atlas"]["wdti_mD"]["Primary_somatosensory_area,_barrel_field,_layer_6b"]
        +data["/P56_atlas"]["wdti_mD"]["Primary_somatosensory_area,_lower_limb,_layer_1"]
        +data["/P56_atlas"]["wdti_mD"]["Primary_somatosensory_area,_lower_limb,_layer_2/3"]
        +data["/P56_atlas"]["wdti_mD"]["Primary_somatosensory_area,_lower_limb,_layer_4"]
        +data["/P56_atlas"]["wdti_mD"]["Primary_somatosensory_area,_lower_limb,_layer_5"]
        +data["/P56_atlas"]["wdti_mD"]["Primary_somatosensory_area,_lower_limb,_layer_6a"]
        +data["/P56_atlas"]["wdti_mD"]["Primary_somatosensory_area,_lower_limb,_layer_6b"]
        +data["/P56_atlas"]["wdti_mD"]["Primary_somatosensory_area,_mouth,_layer_1"]
        +data["/P56_atlas"]["wdti_mD"]["Primary_somatosensory_area,_mouth,_layer_2/3"]
        +data["/P56_atlas"]["wdti_mD"]["Primary_somatosensory_area,_mouth,_layer_4"]
        +data["/P56_atlas"]["wdti_mD"]["Primary_somatosensory_area,_mouth,_layer_5"]
        +data["/P56_atlas"]["wdti_mD"]["Primary_somatosensory_area,_mouth,_layer_6a"]
        +data["/P56_atlas"]["wdti_mD"]["Primary_somatosensory_area,_mouth,_layer_6b"]
        +data["/P56_atlas"]["wdti_mD"]["Primary_somatosensory_area,_upper_limb,_layer_1"]
        +data["/P56_atlas"]["wdti_mD"]["Primary_somatosensory_area,_upper_limb,_layer_2/3"]
        +data["/P56_atlas"]["wdti_mD"]["Primary_somatosensory_area,_upper_limb,_layer_4"]
        +data["/P56_atlas"]["wdti_mD"]["Primary_somatosensory_area,_upper_limb,_layer_5"]
        +data["/P56_atlas"]["wdti_mD"]["Primary_somatosensory_area,_upper_limb,_layer_6a"]
        +data["/P56_atlas"]["wdti_mD"]["Primary_somatosensory_area,_upper_limb,_layer_6b"]
        +data["/P56_atlas"]["wdti_mD"]["Primary_somatosensory_area,_trunk,_layer_1"]
        +data["/P56_atlas"]["wdti_mD"]["Primary_somatosensory_area,_trunk,_layer_2/3"]
        +data["/P56_atlas"]["wdti_mD"]["Primary_somatosensory_area,_trunk,_layer_4"]
        +data["/P56_atlas"]["wdti_mD"]["Primary_somatosensory_area,_trunk,_layer_5"]
        +data["/P56_atlas"]["wdti_mD"]["Primary_somatosensory_area,_trunk,_layer_6a"]
        +data["/P56_atlas"]["wdti_mD"]["Primary_somatosensory_area,_trunk,_layer_6b"]
        +data["/P56_atlas"]["wdti_mD"]["Primary_somatosensory_area,_unassigned,_layer_1"]
        +data["/P56_atlas"]["wdti_mD"]["Primary_somatosensory_area,_unassigned,_layer_2/3"]
        +data["/P56_atlas"]["wdti_mD"]["Primary_somatosensory_area,_unassigned,_layer_4"]
        +data["/P56_atlas"]["wdti_mD"]["Primary_somatosensory_area,_unassigned,_layer_5"]
        +data["/P56_atlas"]["wdti_mD"]["Primary_somatosensory_area,_unassigned,_layer_6a"]
        +data["/P56_atlas"]["wdti_mD"]["Primary_somatosensory_area,_unassigned,_layer_6b"]
        +data["/P56_atlas"]["wdti_mD"]["Supplemental_somatosensory_area,_layer_1"]
        +data["/P56_atlas"]["wdti_mD"]["Supplemental_somatosensory_area,_layer_2/3"]
        +data["/P56_atlas"]["wdti_mD"]["Supplemental_somatosensory_area,_layer_4"]
        +data["/P56_atlas"]["wdti_mD"]["Supplemental_somatosensory_area,_layer_5"]
        +data["/P56_atlas"]["wdti_mD"]["Supplemental_somatosensory_area,_layer_6a"]
        +data["/P56_atlas"]["wdti_mD"]["Supplemental_somatosensory_area,_layer_6b"]
        +data["/P56_atlas"]["wdti_mD"]["Gustatory_areas,_layer_1"]
        +data["/P56_atlas"]["wdti_mD"]["Gustatory_areas,_layer_2/3"]
        +data["/P56_atlas"]["wdti_mD"]["Gustatory_areas,_layer_4"]
        +data["/P56_atlas"]["wdti_mD"]["Gustatory_areas,_layer_5"]
        +data["/P56_atlas"]["wdti_mD"]["Gustatory_areas,_layer_6a"]
        +data["/P56_atlas"]["wdti_mD"]["Gustatory_areas,_layer_6b"]
        +data["/P56_atlas"]["wdti_mD"]["Visceral_area,_layer_1"]
        +data["/P56_atlas"]["wdti_mD"]["Visceral_area,_layer_2/3"]
        +data["/P56_atlas"]["wdti_mD"]["Visceral_area,_layer_4"]
        +data["/P56_atlas"]["wdti_mD"]["Visceral_area,_layer_5"]
        +data["/P56_atlas"]["wdti_mD"]["Visceral_area,_layer_6a"]
        +data["/P56_atlas"]["wdti_mD"]["Visceral_area,_layer_6b"]
        +data["/P56_atlas"]["wdti_mD"]["Dorsal_auditory_area,_layer_1"]
        +data["/P56_atlas"]["wdti_mD"]["Dorsal_auditory_area,_layer_2/3"]
        +data["/P56_atlas"]["wdti_mD"]["Dorsal_auditory_area,_layer_4"]
        +data["/P56_atlas"]["wdti_mD"]["Dorsal_auditory_area,_layer_5"]
        +data["/P56_atlas"]["wdti_mD"]["Dorsal_auditory_area,_layer_6a"]
        +data["/P56_atlas"]["wdti_mD"]["Dorsal_auditory_area,_layer_6b"]
        +data["/P56_atlas"]["wdti_mD"]["Primary_auditory_area,_layer_1"]
        +data["/P56_atlas"]["wdti_mD"]["Primary_auditory_area,_layer_2/3"]
        +data["/P56_atlas"]["wdti_mD"]["Primary_auditory_area,_layer_4"]
        +data["/P56_atlas"]["wdti_mD"]["Primary_auditory_area,_layer_5"]
        +data["/P56_atlas"]["wdti_mD"]["Primary_auditory_area,_layer_6a"]
        +data["/P56_atlas"]["wdti_mD"]["Primary_auditory_area,_layer_6b"]
        +data["/P56_atlas"]["wdti_mD"]["Posterior_auditory_area,_layer_1"]
        +data["/P56_atlas"]["wdti_mD"]["Posterior_auditory_area,_layer_2/3"]
        +data["/P56_atlas"]["wdti_mD"]["Posterior_auditory_area,_layer_4"]
        +data["/P56_atlas"]["wdti_mD"]["Posterior_auditory_area,_layer_5"]
        +data["/P56_atlas"]["wdti_mD"]["Posterior_auditory_area,_layer_6a"]
        +data["/P56_atlas"]["wdti_mD"]["Posterior_auditory_area,_layer_6b"]
        +data["/P56_atlas"]["wdti_mD"]["Ventral_auditory_area,_layer_1"]
        +data["/P56_atlas"]["wdti_mD"]["Ventral_auditory_area,_layer_2/3"]
        +data["/P56_atlas"]["wdti_mD"]["Ventral_auditory_area,_layer_4"]
        +data["/P56_atlas"]["wdti_mD"]["Ventral_auditory_area,_layer_5"]
        +data["/P56_atlas"]["wdti_mD"]["Ventral_auditory_area,_layer_6a"]
        +data["/P56_atlas"]["wdti_mD"]["Ventral_auditory_area,_layer_6b"]
        +data["/P56_atlas"]["wdti_mD"]["Anterolateral_visual_area,_layer_1"]
        +data["/P56_atlas"]["wdti_mD"]["Anterolateral_visual_area,_layer_2/3"]
        +data["/P56_atlas"]["wdti_mD"]["Anterolateral_visual_area,_layer_4"]
        +data["/P56_atlas"]["wdti_mD"]["Anterolateral_visual_area,_layer_5"]
        +data["/P56_atlas"]["wdti_mD"]["Anterolateral_visual_area,_layer_6a"]
        +data["/P56_atlas"]["wdti_mD"]["Anterolateral_visual_area,_layer_6b"]
        +data["/P56_atlas"]["wdti_mD"]["Anteromedial_visual_area,_layer_1"]
        +data["/P56_atlas"]["wdti_mD"]["Anteromedial_visual_area,_layer_2/3"]
        +data["/P56_atlas"]["wdti_mD"]["Anteromedial_visual_area,_layer_4"]
        +data["/P56_atlas"]["wdti_mD"]["Anteromedial_visual_area,_layer_5"]
        +data["/P56_atlas"]["wdti_mD"]["Anteromedial_visual_area,_layer_6a"]
        +data["/P56_atlas"]["wdti_mD"]["Anteromedial_visual_area,_layer_6b"]
        +data["/P56_atlas"]["wdti_mD"]["Lateral_visual_area,_layer_1"]
        +data["/P56_atlas"]["wdti_mD"]["Lateral_visual_area,_layer_2/3"]
        +data["/P56_atlas"]["wdti_mD"]["Lateral_visual_area,_layer_4"]
        +data["/P56_atlas"]["wdti_mD"]["Lateral_visual_area,_layer_5"]
        +data["/P56_atlas"]["wdti_mD"]["Lateral_visual_area,_layer_6a"]
        +data["/P56_atlas"]["wdti_mD"]["Lateral_visual_area,_layer_6b"]
        +data["/P56_atlas"]["wdti_mD"]["Primary_visual_area,_layer_1"]
        +data["/P56_atlas"]["wdti_mD"]["Primary_visual_area,_layer_2/3"]
        +data["/P56_atlas"]["wdti_mD"]["Primary_visual_area,_layer_4"]
        +data["/P56_atlas"]["wdti_mD"]["Primary_visual_area,_layer_5"]
        +data["/P56_atlas"]["wdti_mD"]["Primary_visual_area,_layer_6a"]
        +data["/P56_atlas"]["wdti_mD"]["Primary_visual_area,_layer_6b"]
        +data["/P56_atlas"]["wdti_mD"]["Posterolateral_visual_area,_layer_1"]
        +data["/P56_atlas"]["wdti_mD"]["Posterolateral_visual_area,_layer_2/3"]
        +data["/P56_atlas"]["wdti_mD"]["Posterolateral_visual_area,_layer_4"]
        +data["/P56_atlas"]["wdti_mD"]["Posterolateral_visual_area,_layer_5"]
        +data["/P56_atlas"]["wdti_mD"]["Posterolateral_visual_area,_layer_6a"]
        +data["/P56_atlas"]["wdti_mD"]["Posterolateral_visual_area,_layer_6b"]
        +data["/P56_atlas"]["wdti_mD"]["posteromedial_visual_area,_layer_1"]
        +data["/P56_atlas"]["wdti_mD"]["posteromedial_visual_area,_layer_2/3"]
        +data["/P56_atlas"]["wdti_mD"]["posteromedial_visual_area,_layer_4"]
        +data["/P56_atlas"]["wdti_mD"]["posteromedial_visual_area,_layer_5"]
        +data["/P56_atlas"]["wdti_mD"]["posteromedial_visual_area,_layer_6a"]
        +data["/P56_atlas"]["wdti_mD"]["posteromedial_visual_area,_layer_6b"]
        +data["/P56_atlas"]["wdti_mD"]["Anterior_cingulate_area,_dorsal_part,_layer_1"]
        +data["/P56_atlas"]["wdti_mD"]["Anterior_cingulate_area,_dorsal_part,_layer_2/3"]
        +data["/P56_atlas"]["wdti_mD"]["Anterior_cingulate_area,_dorsal_part,_layer_5"]
        +data["/P56_atlas"]["wdti_mD"]["Anterior_cingulate_area,_dorsal_part,_layer_6a"]
        +data["/P56_atlas"]["wdti_mD"]["Anterior_cingulate_area,_dorsal_part,_layer_6b"]
        +data["/P56_atlas"]["wdti_mD"]["Anterior_cingulate_area,_ventral_part,_layer_1"]
        +data["/P56_atlas"]["wdti_mD"]["Anterior_cingulate_area,_ventral_part,_layer_2/3"]
        +data["/P56_atlas"]["wdti_mD"]["Anterior_cingulate_area,_ventral_part,_layer_5"]
        +data["/P56_atlas"]["wdti_mD"]["Anterior_cingulate_area,_ventral_part,_6a"]
        +data["/P56_atlas"]["wdti_mD"]["Anterior_cingulate_area,_ventral_part,_6b"]
        +data["/P56_atlas"]["wdti_mD"]["Prelimbic_area,_layer_1"]
        +data["/P56_atlas"]["wdti_mD"]["Prelimbic_area,_layer_2/3"]
        +data["/P56_atlas"]["wdti_mD"]["Prelimbic_area,_layer_5"]
        +data["/P56_atlas"]["wdti_mD"]["Prelimbic_area,_layer_6a"]
        +data["/P56_atlas"]["wdti_mD"]["Prelimbic_area,_layer_6b"]
        +data["/P56_atlas"]["wdti_mD"]["Infralimbic_area,_layer_1"]
        +data["/P56_atlas"]["wdti_mD"]["Infralimbic_area,_layer_2/3"]
        +data["/P56_atlas"]["wdti_mD"]["Infralimbic_area,_layer_5"]
        +data["/P56_atlas"]["wdti_mD"]["Infralimbic_area,_layer_6a"]
        +data["/P56_atlas"]["wdti_mD"]["Infralimbic_area,_layer_6b"]
        +data["/P56_atlas"]["wdti_mD"]["Orbital_area,_lateral_part,_layer_1"]
        +data["/P56_atlas"]["wdti_mD"]["Orbital_area,_lateral_part,_layer_2/3"]
        +data["/P56_atlas"]["wdti_mD"]["Orbital_area,_lateral_part,_layer_5"]
        +data["/P56_atlas"]["wdti_mD"]["Orbital_area,_lateral_part,_layer_6a"]
        +data["/P56_atlas"]["wdti_mD"]["Orbital_area,_lateral_part,_layer_6b"]
        +data["/P56_atlas"]["wdti_mD"]["Orbital_area,_medial_part,_layer_1"]
        +data["/P56_atlas"]["wdti_mD"]["Orbital_area,_medial_part,_layer_2/3"]
        +data["/P56_atlas"]["wdti_mD"]["Orbital_area,_medial_part,_layer_5"]
        +data["/P56_atlas"]["wdti_mD"]["Orbital_area,_medial_part,_layer_6a"]
        +data["/P56_atlas"]["wdti_mD"]["Orbital_area,_medial_part,_layer_6b"]
        +data["/P56_atlas"]["wdti_mD"]["Orbital_area,_ventrolateral_part,_layer_1"]
        +data["/P56_atlas"]["wdti_mD"]["Orbital_area,_ventrolateral_part,_layer_2/3"]
        +data["/P56_atlas"]["wdti_mD"]["Orbital_area,_ventrolateral_part,_layer_5"]
        +data["/P56_atlas"]["wdti_mD"]["Orbital_area,_ventrolateral_part,_layer_6a"]
        +data["/P56_atlas"]["wdti_mD"]["Orbital_area,_ventrolateral_part,_layer_6b"]
        +data["/P56_atlas"]["wdti_mD"]["Agranular_insular_area,_dorsal_part,_layer_1"]
        +data["/P56_atlas"]["wdti_mD"]["Agranular_insular_area,_dorsal_part,_layer_2/3"]
        +data["/P56_atlas"]["wdti_mD"]["Agranular_insular_area,_dorsal_part,_layer_5"]
        +data["/P56_atlas"]["wdti_mD"]["Agranular_insular_area,_dorsal_part,_layer_6a"]
        +data["/P56_atlas"]["wdti_mD"]["Agranular_insular_area,_dorsal_part,_layer_6b"]
        +data["/P56_atlas"]["wdti_mD"]["Agranular_insular_area,_posterior_part,_layer_1"]
        +data["/P56_atlas"]["wdti_mD"]["Agranular_insular_area,_posterior_part,_layer_2/3"]
        +data["/P56_atlas"]["wdti_mD"]["Agranular_insular_area,_posterior_part,_layer_5"]
        +data["/P56_atlas"]["wdti_mD"]["Agranular_insular_area,_posterior_part,_layer_6a"]
        +data["/P56_atlas"]["wdti_mD"]["Agranular_insular_area,_posterior_part,_layer_6b"]
        +data["/P56_atlas"]["wdti_mD"]["Agranular_insular_area,_ventral_part,_layer_1"]
        +data["/P56_atlas"]["wdti_mD"]["Agranular_insular_area,_ventral_part,_layer_2/3"]
        +data["/P56_atlas"]["wdti_mD"]["Agranular_insular_area,_ventral_part,_layer_5"]
        +data["/P56_atlas"]["wdti_mD"]["Agranular_insular_area,_ventral_part,_layer_6a"]
        +data["/P56_atlas"]["wdti_mD"]["Agranular_insular_area,_ventral_part,_layer_6b"]
        +data["/P56_atlas"]["wdti_mD"]["Retrosplenial_area,_dorsal_part,_layer_1"]
        +data["/P56_atlas"]["wdti_mD"]["Retrosplenial_area,_dorsal_part,_layer_2/3"]
        +data["/P56_atlas"]["wdti_mD"]["Retrosplenial_area,_dorsal_part,_layer_5"]
        +data["/P56_atlas"]["wdti_mD"]["Retrosplenial_area,_dorsal_part,_layer_6a"]
        +data["/P56_atlas"]["wdti_mD"]["Retrosplenial_area,_dorsal_part,_layer_6b"]
        +data["/P56_atlas"]["wdti_mD"]["Retrosplenial_area,_lateral_agranular_part,_layer_1"]
        +data["/P56_atlas"]["wdti_mD"]["Retrosplenial_area,_lateral_agranular_part,_layer_2/3"]
        +data["/P56_atlas"]["wdti_mD"]["Retrosplenial_area,_lateral_agranular_part,_layer_5"]
        +data["/P56_atlas"]["wdti_mD"]["Retrosplenial_area,_lateral_agranular_part,_layer_6a"]
        +data["/P56_atlas"]["wdti_mD"]["Retrosplenial_area,_lateral_agranular_part,_layer_6b"]
        +data["/P56_atlas"]["wdti_mD"]["Retrosplenial_area,_ventral_part,_layer_1"]
        +data["/P56_atlas"]["wdti_mD"]["Retrosplenial_area,_ventral_part,_layer_2/3"]
        +data["/P56_atlas"]["wdti_mD"]["Retrosplenial_area,_ventral_part,_layer_5"]
        +data["/P56_atlas"]["wdti_mD"]["Retrosplenial_area,_ventral_part,_layer_6a"]
        +data["/P56_atlas"]["wdti_mD"]["Retrosplenial_area,_ventral_part,_layer_6b"]
        +data["/P56_atlas"]["wdti_mD"]["Temporal_association_areas,_layer_1"]
        +data["/P56_atlas"]["wdti_mD"]["Temporal_association_areas,_layer_2/3"]
        +data["/P56_atlas"]["wdti_mD"]["Temporal_association_areas,_layer_4"]
        +data["/P56_atlas"]["wdti_mD"]["Temporal_association_areas,_layer_5"]
        +data["/P56_atlas"]["wdti_mD"]["Temporal_association_areas,_layer_6a"]
        +data["/P56_atlas"]["wdti_mD"]["Temporal_association_areas,_layer_6b"]
        +data["/P56_atlas"]["wdti_mD"]["Perirhinal_area,_layer_1"]
        +data["/P56_atlas"]["wdti_mD"]["Perirhinal_area,_layer_2/3"]
        +data["/P56_atlas"]["wdti_mD"]["Perirhinal_area,_layer_5"]
        +data["/P56_atlas"]["wdti_mD"]["Perirhinal_area,_layer_6a"]
        +data["/P56_atlas"]["wdti_mD"]["Perirhinal_area,_layer_6b"]
        +data["/P56_atlas"]["wdti_mD"]["Ectorhinal_area/Layer_1"]
        +data["/P56_atlas"]["wdti_mD"]["Ectorhinal_area/Layer_2/3"]
        +data["/P56_atlas"]["wdti_mD"]["Ectorhinal_area/Layer_5"]
        +data["/P56_atlas"]["wdti_mD"]["Ectorhinal_area/Layer_6a"]
        +data["/P56_atlas"]["wdti_mD"]["Ectorhinal_area/Layer_6b"])/215;

# saving the data in csv file
with open("data_wdti_mD.csv", "w") as csvfile:
    filewriter = csv.writer(csvfile, delimiter=",",quotechar="|", quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(["Region","Group", "dti_mD"])
    for i in range(num_elements):
        filewriter.writerow(["SUB",group_names[i], round(subiculum_list[i],2)])
        filewriter.writerow(["CC",group_names[i], round(corpus_callosum_list[i],2)])
        filewriter.writerow(["CPD",group_names[i], round(cerebal_peduncle_list[i],2)])
        filewriter.writerow(["AC",group_names[i],round(anterior_commissure_list[i],2)])
        filewriter.writerow(["TH",group_names[i], round(thalamus[i],2)])
        filewriter.writerow(["HPR",group_names[i], round(hippocampus[i],2)])
        filewriter.writerow(["CRX",group_names[i], round(cortex[i],2)])

data = pd.read_csv("data_wdti_mD.csv")
data["Region"] = pd.Categorical(data["Region"])
data["Group"] = pd.Categorical(data["Group"])
#generating bar plot of mean values of each region
sns.set(font_scale=3) #sets font size for chart scales
sns.set_style("white")
seq_col_brew = sns.color_palette("Greys", 3)
sns.set_palette(seq_col_brew)
#sns.set_palette(['#000000', '#ABABAB'])

ax=sns.boxplot(x="Region", y="dti_mD", hue="Group", data=data,hue_order=["non-transgene","heterozygote", "homozygote"])
ax = sns.swarmplot(x="Region", y="dti_mD", hue="Group",data=data,dodge=True,hue_order=["non-transgene","heterozygote", "homozygote"],color=".25")
ax.set_ylabel("MD", rotation =90 ) # y-axis label,
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles=handles[0:3], labels=labels[0:3])
ax.set(xlabel=None)
add_stat_annotation(ax, data=data, x="Region", y="dti_mD", hue="Group",hue_order=["non-transgene","heterozygote", "homozygote"],
                    box_pairs=[(("AC", "homozygote"), ("AC", "non-transgene")),
                               (("AC", "homozygote"), ("AC", "heterozygote")),
                                 (("CC", "homozygote"), ("CC", "non-transgene")),
                                (("CC", "homozygote"), ("CC", "heterozygote")),
                           (("CRX", "homozygote"), ("CRX", "heterozygote")),
                               (("CRX", "homozygote"), ("CRX", "non-transgene")),
                               (("CPD", "homozygote"), ("CPD", "heterozygote")),
                          (("CPD", "homozygote"), ("CPD", "non-transgene")),
                                (("HPR", "homozygote"), ("HPR", "heterozygote")),
                               (("HPR", "homozygote"), ("HPR", "non-transgene")),
                            #   (("SUB", "homozygote"), ("SUB", "heterozygote")),
                               (("SUB", "homozygote"), ("SUB", "non-transgene")),
                               (("TH", "homozygote"), ("TH", "heterozygote")),
                               (("TH", "homozygote"), ("TH", "non-transgene"))
                               ],
                    test='t-test_ind', text_format='star', loc='inside',  comparisons_correction=None,verbose=2)

#ax.set(ylim=(0.1, 0.35))
#ax.grid(False)
plt.savefig('MD.png')
plt.show()


#generating list of ROIs
subiculum_list={};
corpus_callosum_list={};
cerebal_peduncle_list={};
internal_capsule_list={};
anterior_commissure_list={};
thalamus={};
hippocampus={};
cortex={};
for i in range(num_elements):
    with open(file_paths[i]) as json_file:
        data = json.load(json_file)
        subiculum_list[i]=data["/P56_atlas"]["wdti_FA"]["Subiculum"];
        corpus_callosum_list[i]=(data["/P56_atlas"]["wdti_FA"]["corpus_callosum,_body"]
        +data["/P56_atlas"]["wdti_FA"]["corpus_callosum,_splenium"]
        +data["/P56_atlas"]["wdti_FA"]["genu_of_corpus_callosum"])/3
        cerebal_peduncle_list[i]=data["/P56_atlas"]["wdti_FA"]["cerebal_peduncle"];
        internal_capsule_list[i]=data["/P56_atlas"]["wdti_FA"]["internal_capsule"];
        anterior_commissure_list[i]=(data["/P56_atlas"]["wdti_FA"]["anterior_commissure,_olfactory_limb"]
        +data["/P56_atlas"]["wdti_FA"]["anterior_commissure,_temporal_limb"])/2
        thalamus[i]=data["/P56_atlas"]["wdti_FA"]["Thalamus"];
        hippocampus[i]=data["/P56_atlas"]["wdti_FA"]["Dentate_gyrus,_granule_cell_layer"]
        +data["/P56_atlas"]["wdti_FA"]["Dentate_gyrus,_molecular_layer"]
        +data["/P56_atlas"]["wdti_FA"]["Dentate_gyrus,_polymorph_layer"]
        +data["/P56_atlas"]["wdti_FA"]["Field_CA1"]
        +data["/P56_atlas"]["wdti_FA"]["Field_CA2"]
        +data["/P56_atlas"]["wdti_FA"]["Field_CA3"]
        +data["/P56_atlas"]["wdti_FA"]["Fasciola_cinerea"]
        cortex[i]=(data["/P56_atlas"]["wdti_FA"]["Frontal_pole,_layer_1"]
        +data["/P56_atlas"]["wdti_FA"]["Frontal_pole,_layer_2/3"]
        +data["/P56_atlas"]["wdti_FA"]["Frontal_pole,_layer_5"]
        +data["/P56_atlas"]["wdti_FA"]["Frontal_pole,_layer_6a"]
        +data["/P56_atlas"]["wdti_FA"]["Primary_motor_area,_Layer_1"]
        +data["/P56_atlas"]["wdti_FA"]["Primary_motor_area,_Layer_2/3"]
        +data["/P56_atlas"]["wdti_FA"]["Primary_motor_area,_Layer_5"]
        +data["/P56_atlas"]["wdti_FA"]["Primary_motor_area,_Layer_6a"]
        +data["/P56_atlas"]["wdti_FA"]["Primary_motor_area,_Layer_6b"]
        +data["/P56_atlas"]["wdti_FA"]["Secondary_motor_area,_layer_1"]
        +data["/P56_atlas"]["wdti_FA"]["Secondary_motor_area,_layer_2/3"]
        +data["/P56_atlas"]["wdti_FA"]["Secondary_motor_area,_layer_5"]
        +data["/P56_atlas"]["wdti_FA"]["Secondary_motor_area,_layer_6a"]
        +data["/P56_atlas"]["wdti_FA"]["Secondary_motor_area,_layer_6b"]
        +data["/P56_atlas"]["wdti_FA"]["Primary_somatosensory_area,_nose,_layer_1"]
        +data["/P56_atlas"]["wdti_FA"]["Primary_somatosensory_area,_nose,_layer_2/3"]
        +data["/P56_atlas"]["wdti_FA"]["Primary_somatosensory_area,_nose,_layer_4"]
        +data["/P56_atlas"]["wdti_FA"]["Primary_somatosensory_area,_nose,_layer_5"]
        +data["/P56_atlas"]["wdti_FA"]["Primary_somatosensory_area,_nose,_layer_6a"]
        +data["/P56_atlas"]["wdti_FA"]["Primary_somatosensory_area,_nose,_layer_6b"]
        +data["/P56_atlas"]["wdti_FA"]["Primary_somatosensory_area,_barrel_field,_layer_1"]
        +data["/P56_atlas"]["wdti_FA"]["Primary_somatosensory_area,_barrel_field,_layer_2/3"]
        +data["/P56_atlas"]["wdti_FA"]["Primary_somatosensory_area,_barrel_field,_layer_4"]
        +data["/P56_atlas"]["wdti_FA"]["Primary_somatosensory_area,_barrel_field,_layer_5"]
        +data["/P56_atlas"]["wdti_FA"]["Primary_somatosensory_area,_barrel_field,_layer_6a"]
        +data["/P56_atlas"]["wdti_FA"]["Primary_somatosensory_area,_barrel_field,_layer_6b"]
        +data["/P56_atlas"]["wdti_FA"]["Primary_somatosensory_area,_lower_limb,_layer_1"]
        +data["/P56_atlas"]["wdti_FA"]["Primary_somatosensory_area,_lower_limb,_layer_2/3"]
        +data["/P56_atlas"]["wdti_FA"]["Primary_somatosensory_area,_lower_limb,_layer_4"]
        +data["/P56_atlas"]["wdti_FA"]["Primary_somatosensory_area,_lower_limb,_layer_5"]
        +data["/P56_atlas"]["wdti_FA"]["Primary_somatosensory_area,_lower_limb,_layer_6a"]
        +data["/P56_atlas"]["wdti_FA"]["Primary_somatosensory_area,_lower_limb,_layer_6b"]
        +data["/P56_atlas"]["wdti_FA"]["Primary_somatosensory_area,_mouth,_layer_1"]
        +data["/P56_atlas"]["wdti_FA"]["Primary_somatosensory_area,_mouth,_layer_2/3"]
        +data["/P56_atlas"]["wdti_FA"]["Primary_somatosensory_area,_mouth,_layer_4"]
        +data["/P56_atlas"]["wdti_FA"]["Primary_somatosensory_area,_mouth,_layer_5"]
        +data["/P56_atlas"]["wdti_FA"]["Primary_somatosensory_area,_mouth,_layer_6a"]
        +data["/P56_atlas"]["wdti_FA"]["Primary_somatosensory_area,_mouth,_layer_6b"]
        +data["/P56_atlas"]["wdti_FA"]["Primary_somatosensory_area,_upper_limb,_layer_1"]
        +data["/P56_atlas"]["wdti_FA"]["Primary_somatosensory_area,_upper_limb,_layer_2/3"]
        +data["/P56_atlas"]["wdti_FA"]["Primary_somatosensory_area,_upper_limb,_layer_4"]
        +data["/P56_atlas"]["wdti_FA"]["Primary_somatosensory_area,_upper_limb,_layer_5"]
        +data["/P56_atlas"]["wdti_FA"]["Primary_somatosensory_area,_upper_limb,_layer_6a"]
        +data["/P56_atlas"]["wdti_FA"]["Primary_somatosensory_area,_upper_limb,_layer_6b"]
        +data["/P56_atlas"]["wdti_FA"]["Primary_somatosensory_area,_trunk,_layer_1"]
        +data["/P56_atlas"]["wdti_FA"]["Primary_somatosensory_area,_trunk,_layer_2/3"]
        +data["/P56_atlas"]["wdti_FA"]["Primary_somatosensory_area,_trunk,_layer_4"]
        +data["/P56_atlas"]["wdti_FA"]["Primary_somatosensory_area,_trunk,_layer_5"]
        +data["/P56_atlas"]["wdti_FA"]["Primary_somatosensory_area,_trunk,_layer_6a"]
        +data["/P56_atlas"]["wdti_FA"]["Primary_somatosensory_area,_trunk,_layer_6b"]
        +data["/P56_atlas"]["wdti_FA"]["Primary_somatosensory_area,_unassigned,_layer_1"]
        +data["/P56_atlas"]["wdti_FA"]["Primary_somatosensory_area,_unassigned,_layer_2/3"]
        +data["/P56_atlas"]["wdti_FA"]["Primary_somatosensory_area,_unassigned,_layer_4"]
        +data["/P56_atlas"]["wdti_FA"]["Primary_somatosensory_area,_unassigned,_layer_5"]
        +data["/P56_atlas"]["wdti_FA"]["Primary_somatosensory_area,_unassigned,_layer_6a"]
        +data["/P56_atlas"]["wdti_FA"]["Primary_somatosensory_area,_unassigned,_layer_6b"]
        +data["/P56_atlas"]["wdti_FA"]["Supplemental_somatosensory_area,_layer_1"]
        +data["/P56_atlas"]["wdti_FA"]["Supplemental_somatosensory_area,_layer_2/3"]
        +data["/P56_atlas"]["wdti_FA"]["Supplemental_somatosensory_area,_layer_4"]
        +data["/P56_atlas"]["wdti_FA"]["Supplemental_somatosensory_area,_layer_5"]
        +data["/P56_atlas"]["wdti_FA"]["Supplemental_somatosensory_area,_layer_6a"]
        +data["/P56_atlas"]["wdti_FA"]["Supplemental_somatosensory_area,_layer_6b"]
        +data["/P56_atlas"]["wdti_FA"]["Gustatory_areas,_layer_1"]
        +data["/P56_atlas"]["wdti_FA"]["Gustatory_areas,_layer_2/3"]
        +data["/P56_atlas"]["wdti_FA"]["Gustatory_areas,_layer_4"]
        +data["/P56_atlas"]["wdti_FA"]["Gustatory_areas,_layer_5"]
        +data["/P56_atlas"]["wdti_FA"]["Gustatory_areas,_layer_6a"]
        +data["/P56_atlas"]["wdti_FA"]["Gustatory_areas,_layer_6b"]
        +data["/P56_atlas"]["wdti_FA"]["Visceral_area,_layer_1"]
        +data["/P56_atlas"]["wdti_FA"]["Visceral_area,_layer_2/3"]
        +data["/P56_atlas"]["wdti_FA"]["Visceral_area,_layer_4"]
        +data["/P56_atlas"]["wdti_FA"]["Visceral_area,_layer_5"]
        +data["/P56_atlas"]["wdti_FA"]["Visceral_area,_layer_6a"]
        +data["/P56_atlas"]["wdti_FA"]["Visceral_area,_layer_6b"]
        +data["/P56_atlas"]["wdti_FA"]["Dorsal_auditory_area,_layer_1"]
        +data["/P56_atlas"]["wdti_FA"]["Dorsal_auditory_area,_layer_2/3"]
        +data["/P56_atlas"]["wdti_FA"]["Dorsal_auditory_area,_layer_4"]
        +data["/P56_atlas"]["wdti_FA"]["Dorsal_auditory_area,_layer_5"]
        +data["/P56_atlas"]["wdti_FA"]["Dorsal_auditory_area,_layer_6a"]
        +data["/P56_atlas"]["wdti_FA"]["Dorsal_auditory_area,_layer_6b"]
        +data["/P56_atlas"]["wdti_FA"]["Primary_auditory_area,_layer_1"]
        +data["/P56_atlas"]["wdti_FA"]["Primary_auditory_area,_layer_2/3"]
        +data["/P56_atlas"]["wdti_FA"]["Primary_auditory_area,_layer_4"]
        +data["/P56_atlas"]["wdti_FA"]["Primary_auditory_area,_layer_5"]
        +data["/P56_atlas"]["wdti_FA"]["Primary_auditory_area,_layer_6a"]
        +data["/P56_atlas"]["wdti_FA"]["Primary_auditory_area,_layer_6b"]
        +data["/P56_atlas"]["wdti_FA"]["Posterior_auditory_area,_layer_1"]
        +data["/P56_atlas"]["wdti_FA"]["Posterior_auditory_area,_layer_2/3"]
        +data["/P56_atlas"]["wdti_FA"]["Posterior_auditory_area,_layer_4"]
        +data["/P56_atlas"]["wdti_FA"]["Posterior_auditory_area,_layer_5"]
        +data["/P56_atlas"]["wdti_FA"]["Posterior_auditory_area,_layer_6a"]
        +data["/P56_atlas"]["wdti_FA"]["Posterior_auditory_area,_layer_6b"]
        +data["/P56_atlas"]["wdti_FA"]["Ventral_auditory_area,_layer_1"]
        +data["/P56_atlas"]["wdti_FA"]["Ventral_auditory_area,_layer_2/3"]
        +data["/P56_atlas"]["wdti_FA"]["Ventral_auditory_area,_layer_4"]
        +data["/P56_atlas"]["wdti_FA"]["Ventral_auditory_area,_layer_5"]
        +data["/P56_atlas"]["wdti_FA"]["Ventral_auditory_area,_layer_6a"]
        +data["/P56_atlas"]["wdti_FA"]["Ventral_auditory_area,_layer_6b"]
        +data["/P56_atlas"]["wdti_FA"]["Anterolateral_visual_area,_layer_1"]
        +data["/P56_atlas"]["wdti_FA"]["Anterolateral_visual_area,_layer_2/3"]
        +data["/P56_atlas"]["wdti_FA"]["Anterolateral_visual_area,_layer_4"]
        +data["/P56_atlas"]["wdti_FA"]["Anterolateral_visual_area,_layer_5"]
        +data["/P56_atlas"]["wdti_FA"]["Anterolateral_visual_area,_layer_6a"]
        +data["/P56_atlas"]["wdti_FA"]["Anterolateral_visual_area,_layer_6b"]
        +data["/P56_atlas"]["wdti_FA"]["Anteromedial_visual_area,_layer_1"]
        +data["/P56_atlas"]["wdti_FA"]["Anteromedial_visual_area,_layer_2/3"]
        +data["/P56_atlas"]["wdti_FA"]["Anteromedial_visual_area,_layer_4"]
        +data["/P56_atlas"]["wdti_FA"]["Anteromedial_visual_area,_layer_5"]
        +data["/P56_atlas"]["wdti_FA"]["Anteromedial_visual_area,_layer_6a"]
        +data["/P56_atlas"]["wdti_FA"]["Anteromedial_visual_area,_layer_6b"]
        +data["/P56_atlas"]["wdti_FA"]["Lateral_visual_area,_layer_1"]
        +data["/P56_atlas"]["wdti_FA"]["Lateral_visual_area,_layer_2/3"]
        +data["/P56_atlas"]["wdti_FA"]["Lateral_visual_area,_layer_4"]
        +data["/P56_atlas"]["wdti_FA"]["Lateral_visual_area,_layer_5"]
        +data["/P56_atlas"]["wdti_FA"]["Lateral_visual_area,_layer_6a"]
        +data["/P56_atlas"]["wdti_FA"]["Lateral_visual_area,_layer_6b"]
        +data["/P56_atlas"]["wdti_FA"]["Primary_visual_area,_layer_1"]
        +data["/P56_atlas"]["wdti_FA"]["Primary_visual_area,_layer_2/3"]
        +data["/P56_atlas"]["wdti_FA"]["Primary_visual_area,_layer_4"]
        +data["/P56_atlas"]["wdti_FA"]["Primary_visual_area,_layer_5"]
        +data["/P56_atlas"]["wdti_FA"]["Primary_visual_area,_layer_6a"]
        +data["/P56_atlas"]["wdti_FA"]["Primary_visual_area,_layer_6b"]
        +data["/P56_atlas"]["wdti_FA"]["Posterolateral_visual_area,_layer_1"]
        +data["/P56_atlas"]["wdti_FA"]["Posterolateral_visual_area,_layer_2/3"]
        +data["/P56_atlas"]["wdti_FA"]["Posterolateral_visual_area,_layer_4"]
        +data["/P56_atlas"]["wdti_FA"]["Posterolateral_visual_area,_layer_5"]
        +data["/P56_atlas"]["wdti_FA"]["Posterolateral_visual_area,_layer_6a"]
        +data["/P56_atlas"]["wdti_FA"]["Posterolateral_visual_area,_layer_6b"]
        +data["/P56_atlas"]["wdti_FA"]["posteromedial_visual_area,_layer_1"]
        +data["/P56_atlas"]["wdti_FA"]["posteromedial_visual_area,_layer_2/3"]
        +data["/P56_atlas"]["wdti_FA"]["posteromedial_visual_area,_layer_4"]
        +data["/P56_atlas"]["wdti_FA"]["posteromedial_visual_area,_layer_5"]
        +data["/P56_atlas"]["wdti_FA"]["posteromedial_visual_area,_layer_6a"]
        +data["/P56_atlas"]["wdti_FA"]["posteromedial_visual_area,_layer_6b"]
        +data["/P56_atlas"]["wdti_FA"]["Anterior_cingulate_area,_dorsal_part,_layer_1"]
        +data["/P56_atlas"]["wdti_FA"]["Anterior_cingulate_area,_dorsal_part,_layer_2/3"]
        +data["/P56_atlas"]["wdti_FA"]["Anterior_cingulate_area,_dorsal_part,_layer_5"]
        +data["/P56_atlas"]["wdti_FA"]["Anterior_cingulate_area,_dorsal_part,_layer_6a"]
        +data["/P56_atlas"]["wdti_FA"]["Anterior_cingulate_area,_dorsal_part,_layer_6b"]
        +data["/P56_atlas"]["wdti_FA"]["Anterior_cingulate_area,_ventral_part,_layer_1"]
        +data["/P56_atlas"]["wdti_FA"]["Anterior_cingulate_area,_ventral_part,_layer_2/3"]
        +data["/P56_atlas"]["wdti_FA"]["Anterior_cingulate_area,_ventral_part,_layer_5"]
        +data["/P56_atlas"]["wdti_FA"]["Anterior_cingulate_area,_ventral_part,_6a"]
        +data["/P56_atlas"]["wdti_FA"]["Anterior_cingulate_area,_ventral_part,_6b"]
        +data["/P56_atlas"]["wdti_FA"]["Prelimbic_area,_layer_1"]
        +data["/P56_atlas"]["wdti_FA"]["Prelimbic_area,_layer_2/3"]
        +data["/P56_atlas"]["wdti_FA"]["Prelimbic_area,_layer_5"]
        +data["/P56_atlas"]["wdti_FA"]["Prelimbic_area,_layer_6a"]
        +data["/P56_atlas"]["wdti_FA"]["Prelimbic_area,_layer_6b"]
        +data["/P56_atlas"]["wdti_FA"]["Infralimbic_area,_layer_1"]
        +data["/P56_atlas"]["wdti_FA"]["Infralimbic_area,_layer_2/3"]
        +data["/P56_atlas"]["wdti_FA"]["Infralimbic_area,_layer_5"]
        +data["/P56_atlas"]["wdti_FA"]["Infralimbic_area,_layer_6a"]
        +data["/P56_atlas"]["wdti_FA"]["Infralimbic_area,_layer_6b"]
        +data["/P56_atlas"]["wdti_FA"]["Orbital_area,_lateral_part,_layer_1"]
        +data["/P56_atlas"]["wdti_FA"]["Orbital_area,_lateral_part,_layer_2/3"]
        +data["/P56_atlas"]["wdti_FA"]["Orbital_area,_lateral_part,_layer_5"]
        +data["/P56_atlas"]["wdti_FA"]["Orbital_area,_lateral_part,_layer_6a"]
        +data["/P56_atlas"]["wdti_FA"]["Orbital_area,_lateral_part,_layer_6b"]
        +data["/P56_atlas"]["wdti_FA"]["Orbital_area,_medial_part,_layer_1"]
        +data["/P56_atlas"]["wdti_FA"]["Orbital_area,_medial_part,_layer_2/3"]
        +data["/P56_atlas"]["wdti_FA"]["Orbital_area,_medial_part,_layer_5"]
        +data["/P56_atlas"]["wdti_FA"]["Orbital_area,_medial_part,_layer_6a"]
        +data["/P56_atlas"]["wdti_FA"]["Orbital_area,_medial_part,_layer_6b"]
        +data["/P56_atlas"]["wdti_FA"]["Orbital_area,_ventrolateral_part,_layer_1"]
        +data["/P56_atlas"]["wdti_FA"]["Orbital_area,_ventrolateral_part,_layer_2/3"]
        +data["/P56_atlas"]["wdti_FA"]["Orbital_area,_ventrolateral_part,_layer_5"]
        +data["/P56_atlas"]["wdti_FA"]["Orbital_area,_ventrolateral_part,_layer_6a"]
        +data["/P56_atlas"]["wdti_FA"]["Orbital_area,_ventrolateral_part,_layer_6b"]
        +data["/P56_atlas"]["wdti_FA"]["Agranular_insular_area,_dorsal_part,_layer_1"]
        +data["/P56_atlas"]["wdti_FA"]["Agranular_insular_area,_dorsal_part,_layer_2/3"]
        +data["/P56_atlas"]["wdti_FA"]["Agranular_insular_area,_dorsal_part,_layer_5"]
        +data["/P56_atlas"]["wdti_FA"]["Agranular_insular_area,_dorsal_part,_layer_6a"]
        +data["/P56_atlas"]["wdti_FA"]["Agranular_insular_area,_dorsal_part,_layer_6b"]
        +data["/P56_atlas"]["wdti_FA"]["Agranular_insular_area,_posterior_part,_layer_1"]
        +data["/P56_atlas"]["wdti_FA"]["Agranular_insular_area,_posterior_part,_layer_2/3"]
        +data["/P56_atlas"]["wdti_FA"]["Agranular_insular_area,_posterior_part,_layer_5"]
        +data["/P56_atlas"]["wdti_FA"]["Agranular_insular_area,_posterior_part,_layer_6a"]
        +data["/P56_atlas"]["wdti_FA"]["Agranular_insular_area,_posterior_part,_layer_6b"]
        +data["/P56_atlas"]["wdti_FA"]["Agranular_insular_area,_ventral_part,_layer_1"]
        +data["/P56_atlas"]["wdti_FA"]["Agranular_insular_area,_ventral_part,_layer_2/3"]
        +data["/P56_atlas"]["wdti_FA"]["Agranular_insular_area,_ventral_part,_layer_5"]
        +data["/P56_atlas"]["wdti_FA"]["Agranular_insular_area,_ventral_part,_layer_6a"]
        +data["/P56_atlas"]["wdti_FA"]["Agranular_insular_area,_ventral_part,_layer_6b"]
        +data["/P56_atlas"]["wdti_FA"]["Retrosplenial_area,_dorsal_part,_layer_1"]
        +data["/P56_atlas"]["wdti_FA"]["Retrosplenial_area,_dorsal_part,_layer_2/3"]
        +data["/P56_atlas"]["wdti_FA"]["Retrosplenial_area,_dorsal_part,_layer_5"]
        +data["/P56_atlas"]["wdti_FA"]["Retrosplenial_area,_dorsal_part,_layer_6a"]
        +data["/P56_atlas"]["wdti_FA"]["Retrosplenial_area,_dorsal_part,_layer_6b"]
        +data["/P56_atlas"]["wdti_FA"]["Retrosplenial_area,_lateral_agranular_part,_layer_1"]
        +data["/P56_atlas"]["wdti_FA"]["Retrosplenial_area,_lateral_agranular_part,_layer_2/3"]
        +data["/P56_atlas"]["wdti_FA"]["Retrosplenial_area,_lateral_agranular_part,_layer_5"]
        +data["/P56_atlas"]["wdti_FA"]["Retrosplenial_area,_lateral_agranular_part,_layer_6a"]
        +data["/P56_atlas"]["wdti_FA"]["Retrosplenial_area,_lateral_agranular_part,_layer_6b"]
        +data["/P56_atlas"]["wdti_FA"]["Retrosplenial_area,_ventral_part,_layer_1"]
        +data["/P56_atlas"]["wdti_FA"]["Retrosplenial_area,_ventral_part,_layer_2/3"]
        +data["/P56_atlas"]["wdti_FA"]["Retrosplenial_area,_ventral_part,_layer_5"]
        +data["/P56_atlas"]["wdti_FA"]["Retrosplenial_area,_ventral_part,_layer_6a"]
        +data["/P56_atlas"]["wdti_FA"]["Retrosplenial_area,_ventral_part,_layer_6b"]
        +data["/P56_atlas"]["wdti_FA"]["Temporal_association_areas,_layer_1"]
        +data["/P56_atlas"]["wdti_FA"]["Temporal_association_areas,_layer_2/3"]
        +data["/P56_atlas"]["wdti_FA"]["Temporal_association_areas,_layer_4"]
        +data["/P56_atlas"]["wdti_FA"]["Temporal_association_areas,_layer_5"]
        +data["/P56_atlas"]["wdti_FA"]["Temporal_association_areas,_layer_6a"]
        +data["/P56_atlas"]["wdti_FA"]["Temporal_association_areas,_layer_6b"]
        +data["/P56_atlas"]["wdti_FA"]["Perirhinal_area,_layer_1"]
        +data["/P56_atlas"]["wdti_FA"]["Perirhinal_area,_layer_2/3"]
        +data["/P56_atlas"]["wdti_FA"]["Perirhinal_area,_layer_5"]
        +data["/P56_atlas"]["wdti_FA"]["Perirhinal_area,_layer_6a"]
        +data["/P56_atlas"]["wdti_FA"]["Perirhinal_area,_layer_6b"]
        +data["/P56_atlas"]["wdti_FA"]["Ectorhinal_area/Layer_1"]
        +data["/P56_atlas"]["wdti_FA"]["Ectorhinal_area/Layer_2/3"]
        +data["/P56_atlas"]["wdti_FA"]["Ectorhinal_area/Layer_5"]
        +data["/P56_atlas"]["wdti_FA"]["Ectorhinal_area/Layer_6a"]
        +data["/P56_atlas"]["wdti_FA"]["Ectorhinal_area/Layer_6b"])/215;

# saving the data in csv file
with open("data_wdti_FA.csv", "w") as csvfile:
    filewriter = csv.writer(csvfile, delimiter=",",quotechar="|", quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(["Region","Group", "dti_FA"])
    for i in range(num_elements):
        filewriter.writerow(["SUB", group_names[i], subiculum_list[i]])
        filewriter.writerow(["CC", group_names[i], corpus_callosum_list[i]])
        filewriter.writerow(["CPD", group_names[i], cerebal_peduncle_list[i]])
        filewriter.writerow(["AC", group_names[i], anterior_commissure_list[i]])
        filewriter.writerow(["TH", group_names[i], thalamus[i]])
        filewriter.writerow(["HPR", group_names[i], hippocampus[i]])
        filewriter.writerow(["CRX", group_names[i], cortex[i]])






data = pd.read_csv("data_wdti_FA.csv")
data["Region"] = pd.Categorical(data["Region"])
data["Group"] = pd.Categorical(data["Group"])
#generating bar plot of mean values of each region
sns.set(font_scale=3) #sets font size for chart scales
sns.set_style("white")
seq_col_brew = sns.color_palette("Greys", 3)
sns.set_palette(seq_col_brew)
#sns.set_palette(['#000000', '#ABABAB'])

ax=sns.boxplot(x="Region", y="dti_FA", hue="Group", data=data,hue_order=["non-transgene","heterozygote", "homozygote"])

ax = sns.swarmplot(x="Region", y="dti_FA", hue="Group",data=data,dodge=True,hue_order=["non-transgene","heterozygote", "homozygote"],color=".25")
ax.set_ylabel("FA", rotation =90 ) # y-axis label,
ax.set(xlabel=None)
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles=handles[0:3], labels=labels[0:3])
add_stat_annotation(ax, data=data, x="Region", y="dti_FA", hue="Group",hue_order=["non-transgene","heterozygote", "homozygote"],
                    box_pairs=[#(("AC", "homozygote"), ("AC", "non-transgene")),
                             #   (("AC", "homozygote"), ("AC", "heterozygote")),
                                 (("CC", "homozygote"), ("CC", "non-transgene")),
                                 (("CC", "homozygote"), ("CC", "heterozygote")),
                               (("CRX", "homozygote"), ("CRX", "heterozygote")),
                          #     (("CRX", "homozygote"), ("CRX", "non-transgene")),
                               (("CPD", "homozygote"), ("CPD", "heterozygote")),
                              (("CPD", "homozygote"), ("CPD", "non-transgene")),
                                (("HPR", "homozygote"), ("HPR", "heterozygote")),
                               (("HPR", "homozygote"), ("HPR", "non-transgene")),
                              (("SUB", "homozygote"), ("SUB", "heterozygote")),
                              (("SUB", "homozygote"), ("SUB", "non-transgene")),
                               (("TH", "homozygote"), ("TH", "heterozygote")),
                               (("TH", "homozygote"), ("TH", "non-transgene"))
                               ],
                    test='t-test_ind', text_format='star', loc='inside', comparisons_correction=None, verbose=2)
#ax.set(ylim=(0.1, 0.35))
#ax.grid(False)
plt.savefig('FA.png')
plt.show()
#generating list of ROIs
subiculum_list={};
corpus_callosum_list={};
cerebal_peduncle_list={};
internal_capsule_list={};
anterior_commissure_list={};
thalamus={};
hippocampus={};
cortex={};
for i in range(num_elements):
    with open(file_paths[i]) as json_file:
        data = json.load(json_file)
        subiculum_list[i]=data["/P56_atlas"]["wdti_aD"]["Subiculum"];
        corpus_callosum_list[i]=(data["/P56_atlas"]["wdti_aD"]["corpus_callosum,_body"]
        +data["/P56_atlas"]["wdti_aD"]["corpus_callosum,_splenium"]
        +data["/P56_atlas"]["wdti_aD"]["genu_of_corpus_callosum"])/3
        cerebal_peduncle_list[i]=data["/P56_atlas"]["wdti_aD"]["cerebal_peduncle"];
        internal_capsule_list[i]=data["/P56_atlas"]["wdti_aD"]["internal_capsule"];
        anterior_commissure_list[i]=(data["/P56_atlas"]["wdti_aD"]["anterior_commissure,_olfactory_limb"]
        +data["/P56_atlas"]["wdti_aD"]["anterior_commissure,_temporal_limb"])/2
        thalamus[i]=data["/P56_atlas"]["wdti_aD"]["Thalamus"];
        hippocampus[i]=data["/P56_atlas"]["wdti_aD"]["Dentate_gyrus,_granule_cell_layer"]
        +data["/P56_atlas"]["wdti_aD"]["Dentate_gyrus,_molecular_layer"]
        +data["/P56_atlas"]["wdti_aD"]["Dentate_gyrus,_polymorph_layer"]
        +data["/P56_atlas"]["wdti_aD"]["Field_CA1"]
        +data["/P56_atlas"]["wdti_aD"]["Field_CA2"]
        +data["/P56_atlas"]["wdti_aD"]["Field_CA3"]
        +data["/P56_atlas"]["wdti_aD"]["Fasciola_cinerea"]
        cortex[i]=(data["/P56_atlas"]["wdti_aD"]["Frontal_pole,_layer_1"]
        +data["/P56_atlas"]["wdti_aD"]["Frontal_pole,_layer_2/3"]
        +data["/P56_atlas"]["wdti_aD"]["Frontal_pole,_layer_5"]
        +data["/P56_atlas"]["wdti_aD"]["Frontal_pole,_layer_6a"]
        +data["/P56_atlas"]["wdti_aD"]["Primary_motor_area,_Layer_1"]
        +data["/P56_atlas"]["wdti_aD"]["Primary_motor_area,_Layer_2/3"]
        +data["/P56_atlas"]["wdti_aD"]["Primary_motor_area,_Layer_5"]
        +data["/P56_atlas"]["wdti_aD"]["Primary_motor_area,_Layer_6a"]
        +data["/P56_atlas"]["wdti_aD"]["Primary_motor_area,_Layer_6b"]
        +data["/P56_atlas"]["wdti_aD"]["Secondary_motor_area,_layer_1"]
        +data["/P56_atlas"]["wdti_aD"]["Secondary_motor_area,_layer_2/3"]
        +data["/P56_atlas"]["wdti_aD"]["Secondary_motor_area,_layer_5"]
        +data["/P56_atlas"]["wdti_aD"]["Secondary_motor_area,_layer_6a"]
        +data["/P56_atlas"]["wdti_aD"]["Secondary_motor_area,_layer_6b"]
        +data["/P56_atlas"]["wdti_aD"]["Primary_somatosensory_area,_nose,_layer_1"]
        +data["/P56_atlas"]["wdti_aD"]["Primary_somatosensory_area,_nose,_layer_2/3"]
        +data["/P56_atlas"]["wdti_aD"]["Primary_somatosensory_area,_nose,_layer_4"]
        +data["/P56_atlas"]["wdti_aD"]["Primary_somatosensory_area,_nose,_layer_5"]
        +data["/P56_atlas"]["wdti_aD"]["Primary_somatosensory_area,_nose,_layer_6a"]
        +data["/P56_atlas"]["wdti_aD"]["Primary_somatosensory_area,_nose,_layer_6b"]
        +data["/P56_atlas"]["wdti_aD"]["Primary_somatosensory_area,_barrel_field,_layer_1"]
        +data["/P56_atlas"]["wdti_aD"]["Primary_somatosensory_area,_barrel_field,_layer_2/3"]
        +data["/P56_atlas"]["wdti_aD"]["Primary_somatosensory_area,_barrel_field,_layer_4"]
        +data["/P56_atlas"]["wdti_aD"]["Primary_somatosensory_area,_barrel_field,_layer_5"]
        +data["/P56_atlas"]["wdti_aD"]["Primary_somatosensory_area,_barrel_field,_layer_6a"]
        +data["/P56_atlas"]["wdti_aD"]["Primary_somatosensory_area,_barrel_field,_layer_6b"]
        +data["/P56_atlas"]["wdti_aD"]["Primary_somatosensory_area,_lower_limb,_layer_1"]
        +data["/P56_atlas"]["wdti_aD"]["Primary_somatosensory_area,_lower_limb,_layer_2/3"]
        +data["/P56_atlas"]["wdti_aD"]["Primary_somatosensory_area,_lower_limb,_layer_4"]
        +data["/P56_atlas"]["wdti_aD"]["Primary_somatosensory_area,_lower_limb,_layer_5"]
        +data["/P56_atlas"]["wdti_aD"]["Primary_somatosensory_area,_lower_limb,_layer_6a"]
        +data["/P56_atlas"]["wdti_aD"]["Primary_somatosensory_area,_lower_limb,_layer_6b"]
        +data["/P56_atlas"]["wdti_aD"]["Primary_somatosensory_area,_mouth,_layer_1"]
        +data["/P56_atlas"]["wdti_aD"]["Primary_somatosensory_area,_mouth,_layer_2/3"]
        +data["/P56_atlas"]["wdti_aD"]["Primary_somatosensory_area,_mouth,_layer_4"]
        +data["/P56_atlas"]["wdti_aD"]["Primary_somatosensory_area,_mouth,_layer_5"]
        +data["/P56_atlas"]["wdti_aD"]["Primary_somatosensory_area,_mouth,_layer_6a"]
        +data["/P56_atlas"]["wdti_aD"]["Primary_somatosensory_area,_mouth,_layer_6b"]
        +data["/P56_atlas"]["wdti_aD"]["Primary_somatosensory_area,_upper_limb,_layer_1"]
        +data["/P56_atlas"]["wdti_aD"]["Primary_somatosensory_area,_upper_limb,_layer_2/3"]
        +data["/P56_atlas"]["wdti_aD"]["Primary_somatosensory_area,_upper_limb,_layer_4"]
        +data["/P56_atlas"]["wdti_aD"]["Primary_somatosensory_area,_upper_limb,_layer_5"]
        +data["/P56_atlas"]["wdti_aD"]["Primary_somatosensory_area,_upper_limb,_layer_6a"]
        +data["/P56_atlas"]["wdti_aD"]["Primary_somatosensory_area,_upper_limb,_layer_6b"]
        +data["/P56_atlas"]["wdti_aD"]["Primary_somatosensory_area,_trunk,_layer_1"]
        +data["/P56_atlas"]["wdti_aD"]["Primary_somatosensory_area,_trunk,_layer_2/3"]
        +data["/P56_atlas"]["wdti_aD"]["Primary_somatosensory_area,_trunk,_layer_4"]
        +data["/P56_atlas"]["wdti_aD"]["Primary_somatosensory_area,_trunk,_layer_5"]
        +data["/P56_atlas"]["wdti_aD"]["Primary_somatosensory_area,_trunk,_layer_6a"]
        +data["/P56_atlas"]["wdti_aD"]["Primary_somatosensory_area,_trunk,_layer_6b"]
        +data["/P56_atlas"]["wdti_aD"]["Primary_somatosensory_area,_unassigned,_layer_1"]
        +data["/P56_atlas"]["wdti_aD"]["Primary_somatosensory_area,_unassigned,_layer_2/3"]
        +data["/P56_atlas"]["wdti_aD"]["Primary_somatosensory_area,_unassigned,_layer_4"]
        +data["/P56_atlas"]["wdti_aD"]["Primary_somatosensory_area,_unassigned,_layer_5"]
        +data["/P56_atlas"]["wdti_aD"]["Primary_somatosensory_area,_unassigned,_layer_6a"]
        +data["/P56_atlas"]["wdti_aD"]["Primary_somatosensory_area,_unassigned,_layer_6b"]
        +data["/P56_atlas"]["wdti_aD"]["Supplemental_somatosensory_area,_layer_1"]
        +data["/P56_atlas"]["wdti_aD"]["Supplemental_somatosensory_area,_layer_2/3"]
        +data["/P56_atlas"]["wdti_aD"]["Supplemental_somatosensory_area,_layer_4"]
        +data["/P56_atlas"]["wdti_aD"]["Supplemental_somatosensory_area,_layer_5"]
        +data["/P56_atlas"]["wdti_aD"]["Supplemental_somatosensory_area,_layer_6a"]
        +data["/P56_atlas"]["wdti_aD"]["Supplemental_somatosensory_area,_layer_6b"]
        +data["/P56_atlas"]["wdti_aD"]["Gustatory_areas,_layer_1"]
        +data["/P56_atlas"]["wdti_aD"]["Gustatory_areas,_layer_2/3"]
        +data["/P56_atlas"]["wdti_aD"]["Gustatory_areas,_layer_4"]
        +data["/P56_atlas"]["wdti_aD"]["Gustatory_areas,_layer_5"]
        +data["/P56_atlas"]["wdti_aD"]["Gustatory_areas,_layer_6a"]
        +data["/P56_atlas"]["wdti_aD"]["Gustatory_areas,_layer_6b"]
        +data["/P56_atlas"]["wdti_aD"]["Visceral_area,_layer_1"]
        +data["/P56_atlas"]["wdti_aD"]["Visceral_area,_layer_2/3"]
        +data["/P56_atlas"]["wdti_aD"]["Visceral_area,_layer_4"]
        +data["/P56_atlas"]["wdti_aD"]["Visceral_area,_layer_5"]
        +data["/P56_atlas"]["wdti_aD"]["Visceral_area,_layer_6a"]
        +data["/P56_atlas"]["wdti_aD"]["Visceral_area,_layer_6b"]
        +data["/P56_atlas"]["wdti_aD"]["Dorsal_auditory_area,_layer_1"]
        +data["/P56_atlas"]["wdti_aD"]["Dorsal_auditory_area,_layer_2/3"]
        +data["/P56_atlas"]["wdti_aD"]["Dorsal_auditory_area,_layer_4"]
        +data["/P56_atlas"]["wdti_aD"]["Dorsal_auditory_area,_layer_5"]
        +data["/P56_atlas"]["wdti_aD"]["Dorsal_auditory_area,_layer_6a"]
        +data["/P56_atlas"]["wdti_aD"]["Dorsal_auditory_area,_layer_6b"]
        +data["/P56_atlas"]["wdti_aD"]["Primary_auditory_area,_layer_1"]
        +data["/P56_atlas"]["wdti_aD"]["Primary_auditory_area,_layer_2/3"]
        +data["/P56_atlas"]["wdti_aD"]["Primary_auditory_area,_layer_4"]
        +data["/P56_atlas"]["wdti_aD"]["Primary_auditory_area,_layer_5"]
        +data["/P56_atlas"]["wdti_aD"]["Primary_auditory_area,_layer_6a"]
        +data["/P56_atlas"]["wdti_aD"]["Primary_auditory_area,_layer_6b"]
        +data["/P56_atlas"]["wdti_aD"]["Posterior_auditory_area,_layer_1"]
        +data["/P56_atlas"]["wdti_aD"]["Posterior_auditory_area,_layer_2/3"]
        +data["/P56_atlas"]["wdti_aD"]["Posterior_auditory_area,_layer_4"]
        +data["/P56_atlas"]["wdti_aD"]["Posterior_auditory_area,_layer_5"]
        +data["/P56_atlas"]["wdti_aD"]["Posterior_auditory_area,_layer_6a"]
        +data["/P56_atlas"]["wdti_aD"]["Posterior_auditory_area,_layer_6b"]
        +data["/P56_atlas"]["wdti_aD"]["Ventral_auditory_area,_layer_1"]
        +data["/P56_atlas"]["wdti_aD"]["Ventral_auditory_area,_layer_2/3"]
        +data["/P56_atlas"]["wdti_aD"]["Ventral_auditory_area,_layer_4"]
        +data["/P56_atlas"]["wdti_aD"]["Ventral_auditory_area,_layer_5"]
        +data["/P56_atlas"]["wdti_aD"]["Ventral_auditory_area,_layer_6a"]
        +data["/P56_atlas"]["wdti_aD"]["Ventral_auditory_area,_layer_6b"]
        +data["/P56_atlas"]["wdti_aD"]["Anterolateral_visual_area,_layer_1"]
        +data["/P56_atlas"]["wdti_aD"]["Anterolateral_visual_area,_layer_2/3"]
        +data["/P56_atlas"]["wdti_aD"]["Anterolateral_visual_area,_layer_4"]
        +data["/P56_atlas"]["wdti_aD"]["Anterolateral_visual_area,_layer_5"]
        +data["/P56_atlas"]["wdti_aD"]["Anterolateral_visual_area,_layer_6a"]
        +data["/P56_atlas"]["wdti_aD"]["Anterolateral_visual_area,_layer_6b"]
        +data["/P56_atlas"]["wdti_aD"]["Anteromedial_visual_area,_layer_1"]
        +data["/P56_atlas"]["wdti_aD"]["Anteromedial_visual_area,_layer_2/3"]
        +data["/P56_atlas"]["wdti_aD"]["Anteromedial_visual_area,_layer_4"]
        +data["/P56_atlas"]["wdti_aD"]["Anteromedial_visual_area,_layer_5"]
        +data["/P56_atlas"]["wdti_aD"]["Anteromedial_visual_area,_layer_6a"]
        +data["/P56_atlas"]["wdti_aD"]["Anteromedial_visual_area,_layer_6b"]
        +data["/P56_atlas"]["wdti_aD"]["Lateral_visual_area,_layer_1"]
        +data["/P56_atlas"]["wdti_aD"]["Lateral_visual_area,_layer_2/3"]
        +data["/P56_atlas"]["wdti_aD"]["Lateral_visual_area,_layer_4"]
        +data["/P56_atlas"]["wdti_aD"]["Lateral_visual_area,_layer_5"]
        +data["/P56_atlas"]["wdti_aD"]["Lateral_visual_area,_layer_6a"]
        +data["/P56_atlas"]["wdti_aD"]["Lateral_visual_area,_layer_6b"]
        +data["/P56_atlas"]["wdti_aD"]["Primary_visual_area,_layer_1"]
        +data["/P56_atlas"]["wdti_aD"]["Primary_visual_area,_layer_2/3"]
        +data["/P56_atlas"]["wdti_aD"]["Primary_visual_area,_layer_4"]
        +data["/P56_atlas"]["wdti_aD"]["Primary_visual_area,_layer_5"]
        +data["/P56_atlas"]["wdti_aD"]["Primary_visual_area,_layer_6a"]
        +data["/P56_atlas"]["wdti_aD"]["Primary_visual_area,_layer_6b"]
        +data["/P56_atlas"]["wdti_aD"]["Posterolateral_visual_area,_layer_1"]
        +data["/P56_atlas"]["wdti_aD"]["Posterolateral_visual_area,_layer_2/3"]
        +data["/P56_atlas"]["wdti_aD"]["Posterolateral_visual_area,_layer_4"]
        +data["/P56_atlas"]["wdti_aD"]["Posterolateral_visual_area,_layer_5"]
        +data["/P56_atlas"]["wdti_aD"]["Posterolateral_visual_area,_layer_6a"]
        +data["/P56_atlas"]["wdti_aD"]["Posterolateral_visual_area,_layer_6b"]
        +data["/P56_atlas"]["wdti_aD"]["posteromedial_visual_area,_layer_1"]
        +data["/P56_atlas"]["wdti_aD"]["posteromedial_visual_area,_layer_2/3"]
        +data["/P56_atlas"]["wdti_aD"]["posteromedial_visual_area,_layer_4"]
        +data["/P56_atlas"]["wdti_aD"]["posteromedial_visual_area,_layer_5"]
        +data["/P56_atlas"]["wdti_aD"]["posteromedial_visual_area,_layer_6a"]
        +data["/P56_atlas"]["wdti_aD"]["posteromedial_visual_area,_layer_6b"]
        +data["/P56_atlas"]["wdti_aD"]["Anterior_cingulate_area,_dorsal_part,_layer_1"]
        +data["/P56_atlas"]["wdti_aD"]["Anterior_cingulate_area,_dorsal_part,_layer_2/3"]
        +data["/P56_atlas"]["wdti_aD"]["Anterior_cingulate_area,_dorsal_part,_layer_5"]
        +data["/P56_atlas"]["wdti_aD"]["Anterior_cingulate_area,_dorsal_part,_layer_6a"]
        +data["/P56_atlas"]["wdti_aD"]["Anterior_cingulate_area,_dorsal_part,_layer_6b"]
        +data["/P56_atlas"]["wdti_aD"]["Anterior_cingulate_area,_ventral_part,_layer_1"]
        +data["/P56_atlas"]["wdti_aD"]["Anterior_cingulate_area,_ventral_part,_layer_2/3"]
        +data["/P56_atlas"]["wdti_aD"]["Anterior_cingulate_area,_ventral_part,_layer_5"]
        +data["/P56_atlas"]["wdti_aD"]["Anterior_cingulate_area,_ventral_part,_6a"]
        +data["/P56_atlas"]["wdti_aD"]["Anterior_cingulate_area,_ventral_part,_6b"]
        +data["/P56_atlas"]["wdti_aD"]["Prelimbic_area,_layer_1"]
        +data["/P56_atlas"]["wdti_aD"]["Prelimbic_area,_layer_2/3"]
        +data["/P56_atlas"]["wdti_aD"]["Prelimbic_area,_layer_5"]
        +data["/P56_atlas"]["wdti_aD"]["Prelimbic_area,_layer_6a"]
        +data["/P56_atlas"]["wdti_aD"]["Prelimbic_area,_layer_6b"]
        +data["/P56_atlas"]["wdti_aD"]["Infralimbic_area,_layer_1"]
        +data["/P56_atlas"]["wdti_aD"]["Infralimbic_area,_layer_2/3"]
        +data["/P56_atlas"]["wdti_aD"]["Infralimbic_area,_layer_5"]
        +data["/P56_atlas"]["wdti_aD"]["Infralimbic_area,_layer_6a"]
        +data["/P56_atlas"]["wdti_aD"]["Infralimbic_area,_layer_6b"]
        +data["/P56_atlas"]["wdti_aD"]["Orbital_area,_lateral_part,_layer_1"]
        +data["/P56_atlas"]["wdti_aD"]["Orbital_area,_lateral_part,_layer_2/3"]
        +data["/P56_atlas"]["wdti_aD"]["Orbital_area,_lateral_part,_layer_5"]
        +data["/P56_atlas"]["wdti_aD"]["Orbital_area,_lateral_part,_layer_6a"]
        +data["/P56_atlas"]["wdti_aD"]["Orbital_area,_lateral_part,_layer_6b"]
        +data["/P56_atlas"]["wdti_aD"]["Orbital_area,_medial_part,_layer_1"]
        +data["/P56_atlas"]["wdti_aD"]["Orbital_area,_medial_part,_layer_2/3"]
        +data["/P56_atlas"]["wdti_aD"]["Orbital_area,_medial_part,_layer_5"]
        +data["/P56_atlas"]["wdti_aD"]["Orbital_area,_medial_part,_layer_6a"]
        +data["/P56_atlas"]["wdti_aD"]["Orbital_area,_medial_part,_layer_6b"]
        +data["/P56_atlas"]["wdti_aD"]["Orbital_area,_ventrolateral_part,_layer_1"]
        +data["/P56_atlas"]["wdti_aD"]["Orbital_area,_ventrolateral_part,_layer_2/3"]
        +data["/P56_atlas"]["wdti_aD"]["Orbital_area,_ventrolateral_part,_layer_5"]
        +data["/P56_atlas"]["wdti_aD"]["Orbital_area,_ventrolateral_part,_layer_6a"]
        +data["/P56_atlas"]["wdti_aD"]["Orbital_area,_ventrolateral_part,_layer_6b"]
        +data["/P56_atlas"]["wdti_aD"]["Agranular_insular_area,_dorsal_part,_layer_1"]
        +data["/P56_atlas"]["wdti_aD"]["Agranular_insular_area,_dorsal_part,_layer_2/3"]
        +data["/P56_atlas"]["wdti_aD"]["Agranular_insular_area,_dorsal_part,_layer_5"]
        +data["/P56_atlas"]["wdti_aD"]["Agranular_insular_area,_dorsal_part,_layer_6a"]
        +data["/P56_atlas"]["wdti_aD"]["Agranular_insular_area,_dorsal_part,_layer_6b"]
        +data["/P56_atlas"]["wdti_aD"]["Agranular_insular_area,_posterior_part,_layer_1"]
        +data["/P56_atlas"]["wdti_aD"]["Agranular_insular_area,_posterior_part,_layer_2/3"]
        +data["/P56_atlas"]["wdti_aD"]["Agranular_insular_area,_posterior_part,_layer_5"]
        +data["/P56_atlas"]["wdti_aD"]["Agranular_insular_area,_posterior_part,_layer_6a"]
        +data["/P56_atlas"]["wdti_aD"]["Agranular_insular_area,_posterior_part,_layer_6b"]
        +data["/P56_atlas"]["wdti_aD"]["Agranular_insular_area,_ventral_part,_layer_1"]
        +data["/P56_atlas"]["wdti_aD"]["Agranular_insular_area,_ventral_part,_layer_2/3"]
        +data["/P56_atlas"]["wdti_aD"]["Agranular_insular_area,_ventral_part,_layer_5"]
        +data["/P56_atlas"]["wdti_aD"]["Agranular_insular_area,_ventral_part,_layer_6a"]
        +data["/P56_atlas"]["wdti_aD"]["Agranular_insular_area,_ventral_part,_layer_6b"]
        +data["/P56_atlas"]["wdti_aD"]["Retrosplenial_area,_dorsal_part,_layer_1"]
        +data["/P56_atlas"]["wdti_aD"]["Retrosplenial_area,_dorsal_part,_layer_2/3"]
        +data["/P56_atlas"]["wdti_aD"]["Retrosplenial_area,_dorsal_part,_layer_5"]
        +data["/P56_atlas"]["wdti_aD"]["Retrosplenial_area,_dorsal_part,_layer_6a"]
        +data["/P56_atlas"]["wdti_aD"]["Retrosplenial_area,_dorsal_part,_layer_6b"]
        +data["/P56_atlas"]["wdti_aD"]["Retrosplenial_area,_lateral_agranular_part,_layer_1"]
        +data["/P56_atlas"]["wdti_aD"]["Retrosplenial_area,_lateral_agranular_part,_layer_2/3"]
        +data["/P56_atlas"]["wdti_aD"]["Retrosplenial_area,_lateral_agranular_part,_layer_5"]
        +data["/P56_atlas"]["wdti_aD"]["Retrosplenial_area,_lateral_agranular_part,_layer_6a"]
        +data["/P56_atlas"]["wdti_aD"]["Retrosplenial_area,_lateral_agranular_part,_layer_6b"]
        +data["/P56_atlas"]["wdti_aD"]["Retrosplenial_area,_ventral_part,_layer_1"]
        +data["/P56_atlas"]["wdti_aD"]["Retrosplenial_area,_ventral_part,_layer_2/3"]
        +data["/P56_atlas"]["wdti_aD"]["Retrosplenial_area,_ventral_part,_layer_5"]
        +data["/P56_atlas"]["wdti_aD"]["Retrosplenial_area,_ventral_part,_layer_6a"]
        +data["/P56_atlas"]["wdti_aD"]["Retrosplenial_area,_ventral_part,_layer_6b"]
        +data["/P56_atlas"]["wdti_aD"]["Temporal_association_areas,_layer_1"]
        +data["/P56_atlas"]["wdti_aD"]["Temporal_association_areas,_layer_2/3"]
        +data["/P56_atlas"]["wdti_aD"]["Temporal_association_areas,_layer_4"]
        +data["/P56_atlas"]["wdti_aD"]["Temporal_association_areas,_layer_5"]
        +data["/P56_atlas"]["wdti_aD"]["Temporal_association_areas,_layer_6a"]
        +data["/P56_atlas"]["wdti_aD"]["Temporal_association_areas,_layer_6b"]
        +data["/P56_atlas"]["wdti_aD"]["Perirhinal_area,_layer_1"]
        +data["/P56_atlas"]["wdti_aD"]["Perirhinal_area,_layer_2/3"]
        +data["/P56_atlas"]["wdti_aD"]["Perirhinal_area,_layer_5"]
        +data["/P56_atlas"]["wdti_aD"]["Perirhinal_area,_layer_6a"]
        +data["/P56_atlas"]["wdti_aD"]["Perirhinal_area,_layer_6b"]
        +data["/P56_atlas"]["wdti_aD"]["Ectorhinal_area/Layer_1"]
        +data["/P56_atlas"]["wdti_aD"]["Ectorhinal_area/Layer_2/3"]
        +data["/P56_atlas"]["wdti_aD"]["Ectorhinal_area/Layer_5"]
        +data["/P56_atlas"]["wdti_aD"]["Ectorhinal_area/Layer_6a"]
        +data["/P56_atlas"]["wdti_aD"]["Ectorhinal_area/Layer_6b"])/215;

# saving the data in csv file
with open("data_wdti_aD.csv", "w") as csvfile:
    filewriter = csv.writer(csvfile, delimiter=",",quotechar="|", quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(["Region","Group", "dti_aD"])
    for i in range(num_elements):
        filewriter.writerow(["SUB",group_names[i], subiculum_list[i]])
        filewriter.writerow(["CC",group_names[i], corpus_callosum_list[i]])
        filewriter.writerow(["CPD",group_names[i], cerebal_peduncle_list[i]])
        filewriter.writerow(["AC",group_names[i],anterior_commissure_list[i]])
        filewriter.writerow(["TH",group_names[i], thalamus[i]])
        filewriter.writerow(["HPR",group_names[i], hippocampus[i]])
        filewriter.writerow(["CRX",group_names[i], cortex[i]])
data = pd.read_csv("data_wdti_aD.csv")
data["Region"] = pd.Categorical(data["Region"])
data["Group"] = pd.Categorical(data["Group"])
#generating bar plot of mean values of each region
sns.set(font_scale=3) #sets font size for chart scales
sns.set_style("white")
seq_col_brew = sns.color_palette("Greys", 3)
sns.set_palette(seq_col_brew)
#sns.set_palette(['#000000', '#ABABAB'])

ax=sns.boxplot(x="Region", y="dti_aD", hue="Group", data=data,hue_order=["non-transgene","heterozygote", "homozygote"])
ax = sns.swarmplot(x="Region", y="dti_aD", hue="Group",data=data,dodge=True,hue_order=["non-transgene","heterozygote", "homozygote"],color=".25")
ax.set_ylabel("AD", rotation =90 ) # y-axis label,
ax.set(xlabel=None)
handles, labels = ax.get_legend_handles_labels()
ax.legend(handles=handles[0:3], labels=labels[0:3])
add_stat_annotation(ax, data=data, x="Region", y="dti_aD", hue="Group",hue_order=["non-transgene","heterozygote", "homozygote"],
                    box_pairs=[(("AC", "homozygote"), ("AC", "non-transgene")),
                                (("AC", "homozygote"), ("AC", "heterozygote")),
                                 (("CC", "homozygote"), ("CC", "non-transgene")),
                                (("CC", "homozygote"), ("CC", "heterozygote")),
                              (("CRX", "homozygote"), ("CRX", "heterozygote")),
                               (("CRX", "homozygote"), ("CRX", "non-transgene")),
                               (("CPD", "homozygote"), ("CPD", "heterozygote")),
                              (("CPD", "homozygote"), ("CPD", "non-transgene")),
                               (("HPR", "homozygote"), ("HPR", "heterozygote")),
                               (("HPR", "homozygote"), ("HPR", "non-transgene")),
                            #  (("SUB", "homozygote"), ("SUB", "heterozygote")),
                               (("SUB", "homozygote"), ("SUB", "non-transgene")),
                           #    (("TH", "homozygote"), ("TH", "heterozygote")),
                               (("TH", "homozygote"), ("TH", "non-transgene"))
                               ],
                    test='t-test_ind', text_format='star', loc='inside',  comparisons_correction=None,verbose=2)
#ax.set(ylim=(0.1, 0.35))
#ax.grid(False)
plt.savefig('AD.png')
plt.show()