# ─── PYTHON SEMANTIC TOKEN TEST FILE ──────────────────────────────────────────
# Make sure you have the official "Pylance" extension installed in VS Code!
# Pylance provides the semantic tokens for Python.

# 1. CLASS — should be BOLD 
class DatabaseConnector:
    # 2. CLASS VARIABLE — should be distinct from local variables
    DEFAULT_TIMEOUT = 30 
    
    # 3. PARAMETERS — should be ITALIC (self, host, port)
    def __init__(self, host: str, port: int = 5432):
        # 4. PROPERTIES (self.host) — distinct color
        self.host = host
        self.port = port
        
    # 5. METHODS — distinct function color
    @classmethod # 6. DECORATOR — italic warm color
    def connect(cls, uri: str) -> "DatabaseConnector":
        # 7. VARIABLES — standard variable color
        parsed_host = uri.split(":")[0]
        return cls(parsed_host)

# 8. FUNCTIONS
def fetch_data():
    # 9. BUILT-INS (print, len, dict) — distinct accent color
    print(len("test"))
    
    my_dict = {"key": "value"}
    return my_dict
