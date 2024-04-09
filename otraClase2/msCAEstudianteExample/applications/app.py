import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from infrastructure.controllers import api_rest

if __name__ == "__main__":
    api_rest.app.run(host="0.0.0.0", port=8080, debug=True)
    

