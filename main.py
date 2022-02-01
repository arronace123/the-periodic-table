'''

                            Online Python Interpreter.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''


class table:
    def __init__(self, name, number, atomic, source, form, charge):
        self.name = name
        self.number = number
        self.atomic = atomic
        self.source = source
        self.form = form
        self.charge = charge
        
        
        
#"primordial", from decay synthetic
#s-block f-block d-block p-block
# +1 +2 +3 +4 -3 -2 -1 0
H = table("Hydrogen", 1, 1.008, "alkali", "primordial", 1)
He = table("helium", 2, 4.0026, "alkaline earth metal", "primordial", 0)
Li = table("lithium", 3, 6.94, "alkaline earth metal", "primordial", 1)
Be = table("beryllium", 4, 9.0122, "alkaline, earth metal", "primordial", 2)
B = table("boron", 5, 1.081, "alkaline, earth metal", "primordial", 3)
C = table("carbon", 6, 12.011, "alkaline, earth metal", "primordial", 4)
N = table("nitrogen", 7, 14.007, "nictogin", "primordial", -3)
O = table("oxygen", 8, 15.999, "chalcogen", "primordial", -2)
F = table("Flourine", 9, 18.998, "halogens", "primordial", -1)
Ne = table("neurine", 10, 20.180, "noble", "primordial", 0)
Na = table("sodium", 11, 22.90, "alkali", "primordial", 1)
mG = table("magnesium", 12, 24.305, "alkaline, earth metal", "primordial", 2)
AL = table("aluminum", 13, 26.982, "alkaline, earth metal", "primordial", 3)
Si = table("silicon", 14, 28.085, "alkaline, earth metal", "primordial", 4)
P = table("phosphourus", 15, 30.974, "pnoctogens", "primordial", -3)
S = table("sulfur", 16, 32.06, "chalcogen", "primordial", -2)
CL = table("chlorine", 17, 35.45, "halogens", "primordial", -1)
Ar = table("argon", 18, 39.95, "noble", "primordial", 0)
K = table("potassium", 19, 39.098, "alkali", "primordial", 1)
Ca  = table("calcium", 20, 40.078, "alkaline earth metal","primordial", 2)
Sc = table("scandanium", 21, 44.956, "alkaline earth metal", "primordial", 2)
Ti = table("titanium", 22, 47.867, "alkaline earth metal", "primordial", 2)
V = table("vandanium", 23, 50.942, "alkaline, earth metal", "primordial", 2)
Cr = table("chromium", 24, 51.996, "alkaline, earth metal", "primordial", 2)
Mn = table("maganese", 25, 54.938, "alkaline,earth metal", "primordial", 2)
Fe = table("iron", 26, 55.845, "alkaline, earth metal", "primordial", 2)
Co = table("cobalt", 27, 58.933, "alkaline,earth metal", "primordial",2)
Ni = table("nickle", 28, 58.693, "alkaline, earth metal", "primordial", 2)
Cu = table("copper", 29, 63.546, "alkaline, earth metal", "primordial", 2)
Zn = table("zinc", 30, 65.38, "alkaline, earth metal", "primordial", 2)
Ga = table("galium", 31, 69.723, "alkaline earth metal", "primordial", 3)
Ge = table("gerenium", 32, 72.630, "alkaline earth metal", "primordial", 4)
As = table("arsonic", 33, 74.922, "pnictogen", "primordial", -3)
Se = table("selenium", 34, 78.971, "chalcogen", "primordial", -2)
Br = table("bromine", 35, 79.904, "halogens", "primordial", -1)
Kr = table("krypton",36 ,83.798, "noble gas", "primordial", 0)
Rb = table("rubidium", 37, 85.468, "alkali", "primordial", 1)
Sr = table("strontonium", 38, 87.62, "alkaline earth metal","primordial", 2)
Y = table("yttrium", 39, 88.906, "alkaline earth metal", "primordial", 2)
Zr = table("zirconium", 40, 91.224, "alkaline earth metal", "primordial", 2)
Nb = table("niobium", 41, 92.906, "alkaline earth metal", "primordial", 2)
Mo = table("molybdenum",42, 95.95, "alkaline earth metal", "primordial", 2)
Tc = table("technetium", 43, 97, "alkaline earth metal", "from decay", 2)
Ru = table("ruthenium", 44, 101.07, "alkaline earth metal", "primordial", 2)
Rh = table("rhodium", 45, 102.91, "alkaline earth metal", "primordial", 2)
pd = table("paladium", 46, 106.42, "alkaline earth metal", "primordial", 2)
Ag = table("silver", 47, 107.87, "alkaline earth metal", "primordial", 2)
Cd = table("cadmium", 48, 112.41, "alkaline earth metal", "primordial", 2)
In = table("indium", 49, 114.82, "alkaline earth metal", "primordial", 3)
Sn = table("tin", 50, 118.71, "alkaline earth metal", "primordial", 4)
Sb = table("antimony", 51, 121.76, "pnictogen", "primordial", -3)
Te = table("tellerium", 52, 127.60, "chalcogen","primordial", -2)
I = table("iodine", 53, 126.90, "halogen", "primordial", -1)
Xe = table("xenon", 54, 131.29, "noble gas", "primordial", 0)
cs = table("cesium",55, 132.91, "alkali", "primordial", 1)
Ba = table("barium", 56, 137.33, "alkaline earth metal", "primordial", 2)
La = table("lathanum", 57, 138.91, "alkaline earth metal", "primordial", 2)
Ce = table("cerium", 58, 140.12, "alkaline earth metal", "primordial", 2)
Pr = table("praseogymium", 59, 140.91, "alkaline earth metal", "primordial", 2)
Nd = table("neodymium", 60, 144.24, "alkaline earth metal", "primordial", 2)
Pm = table("promethium", 61, 145, "alkaline earth metal","from decay", 2)
Sm = table("samarium", 62, 150.36, "alkaline earth metal", "primordial", 2)
Eu = table("europium", 63, 151.96, "alkaline earth metal", "primordial", 2)
Gd = table("gadolinium", 64, 157.25, "alkaline earth metal", "primordial", 2)
Tb = table("terbium", 65, 158.93, "alkaline earth metal", "primordial", 2)
Dy = table("dysprosium", 66, 162.50, "alkaline earth metal", "primordial",2)
Ho = table("holmium", 67, 164.93, "alkaline earth metal", "primordial", 2)
Er = table("erbium", 68, 167.26, "alkaline earth metal", "primordial", 2)
Tm = table("thullum", 69, 168.93, "pnictogen", "primordial", 2)
Yb = table("ytterbium", 70, 173.05, "chalcogen", "primordial", 2)
Lu = table("lutenium", 71, 174.97, "alkaline earth metal", "primordial", 2)
Hf = table("hafnium", 72, 178.49, "alkaline earth metal", "primordial", 2)
Ta = table("tantalum", 73, 180.95, "alkaline earth metal", "primordial", 2)
w = table("tungsten", 74, 183.84, "alkaline earth metal", "primordial", 2)
Re = table("rhenium", 75, 185.21, "alkaline earth metal", "primordial", 2)
Os = table("osmium", 76, 190.23, "alkaline earth metal", "primordial", 2)
Ir = table("iridium", 77, 192.22, "alkaline earth metal", "primordial", 2)
Pt = table("platinum", 78, 195.08, "alkaline earth metal", "primordial", 2)
Au = table("gold", 79, 196.97, "alkaline earth metal", "primordial", 2)
Hg = table("mercury", 80, 200.59, "alkaline earth metal", "primordial", 2)
Ti = table("thallium", 81, 204.38, "alkaline earth metal", "primordial", 3)
Pb = table("lead", 82, 207.2, "alkaline earth metal", "primordial", 4)
Bi = table("bismuth", 83, 208.98, "pnictogen", "primordial", -3)
Po = table("polonium", 84, 209, "chalcogen", "from decay", -2)
At = table("astatine", 85, 210, "halogen", "from decay", 1)
Rn = table("radon", 86, 222, "noble gas", "from decay", 0)
Fr = table("francium", 87, 223, "alkali", "from decay", 1)
Ra = table("radium", 88, 226, "alkaline earth metal", "from decay",2)
Ac = table("actinium", 89, 227, "alkaline earth metal", "from decay",2)
Th = table("thorium", 90, 232.04, "alkaline earth metal", "primordial", 2)
Pa = table("protacinium", 91, 231.04, "alkaline earth metal", "from decay", 2)
U = table("uranium", 92, 23.03, "alkaline earth metal", "primordial", 2)
Np = table("neptunium", 93, 237, "alkaline earth metal", "from decay", 2)
Pu = table("plutonium", 94, 244, "alkaline earth metal", "from decay", 2)
Am = table("amercium", 95, 243, "alkaline earth metal", "synthetic", 2)
Cm = table("curium", 96, 247, "alkaline earth metal", "synthetic", 2)
Bk = table("berkelium", 97, 247, "alkaline earth metal", "synthetic", 2)
Cf = table("califonium", 98, 251, "alkaline earth metal", "synthetic", 2)
Es = table("einsteinium", 99, 252, "alkaline earth metal", "synthetic", 2)
Fm = table("fernium", 100, 257, "alkaline earth metal", "synthetic", 2)
Md = table("mendelevium", 101, 258, "pnictogen", "synthetic", 2)
No = table("nobelium", 102, 259, "chalcogen", "synthetic", 2)
Lr = table("lawrencium", 103, 266, "alkaline earth metal", "synthetic", 2)
Rf = table("rutherfordiam", 104, 267,"alkaline earth metal", "synthetic", 2)
Db = table("dubnium", 105, 268,"alkaline earth metal", "synthetic", 2)
Sg = table("sea-borgium", 106, 269, "alkaline earth metal", "synthetic", 2)
Bh = table("bohrium", 107, 270, "alkaline earth metal", "synthetic", 2)
Hs = table("hassium", 108, 269, "alkaline earth metal", "synthetic", 2)
Mt = table("maitnerium", 109, 270, "alkaline earth metal", "synthetic", 2)
Ds = table("darmstadtium", 110, 281, "alkaline earth metal", "synthetic", 2)
Rg = table("roentgenium", 111, 282, "alkaline earth metal", "synthetic", 2)
Cn = table("copernecium", 112, 285, "alkaline earth metal", "synthetic", 2)
Nh = table("nihonium", 113, 285, "alkaline earth metal", "synthetic", 3)
FL = table("flervonium", 114,286, "alkaline earth metal", "synthetic", 4)
Mc = table("moscovium", 115, 290, "pnictogen", "synthetic", -3)
Lv = table("livermorium", 116, 293, "chalcogen", "synthetic", -2)
Ts = table("tennessine", 117, 294, "halogens", "synthetic", -1)
Og = table("oga nesson", 118, 294, "noble gas", "synthetic", 0)





    



