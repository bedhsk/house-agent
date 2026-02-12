# =========================================
#  CONFIGURACION
# =========================================

LADO        = 7
ALTO_PARED  = 4

# Distancia desde el jugador al inicio de la casa
OFFSET_X = 3
OFFSET_Z = 3

# Materiales
MAT_PARED   = PLANKS_OAK
MAT_TECHO   = PLANKS_SPRUCE
MAT_VENTANA = GLASS_PANE
MAT_LUZ     = TORCH

# =========================================
#  FUNCIONES AUXILIARES
# =========================================

def dar_material(material, slot, cantidad=64):
    """Carga mater"""