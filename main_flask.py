import base64
from io import BytesIO

from rdkit import Chem
from rdkit.Chem import Draw

from flask import Flask, render_template, abort, request
import json
app = Flask(__name__)

# For test
lista =[
'CN1C=NC2=C1C(=O)N(C(=O)N2C)C',
'O=C(C)Oc1ccccc1C(=O)O',
'CC(=O)Nc1ccc(O)cc1',]


'''
#E.G: base64 for test
bb='iVBORw0KGgoAAAANSUhEUgAAASwAAAEsCAIAAAD2HxkiAAAFeUlEQVR4nO3cUVLbSBRAUWlqdpT97yCsSfPhKY8DNthG1u1mzvkKBZWIR191C0PWbdsWoPNXfQHwfydCiIkQYiKEmAghJkKIiRBiIoSYCCEmQoiJEGIihJgIISZCiIkQYiKEmAghJkKIiRBiIoSYCCEmQoiJEGIihJgIISZCiIkQYiKEmAghJkKIiRBiIoSYCCEmQoiJEGIihJgIISZCiIkQYiKEmAghJkKIiRBiIoSYCCEmQoiJEGIihJgIISZCiIkQYiKEmAghJkKIiRBiIoSYCCEmQoiJEGIihJgIISZCiIkQYiKEmAghJkKIiRBiIoSYCCEmQoiJEGIihJgIISZCiIkQYiKEmAghJkKIiRBiIoSYCCEmQoiJEGIihJgIISZCiIkQYiKEmAghJkKIiRBiIoSYCCEmQoiJEGIihJgIISZCiIkQYiKEmAghJkKIiRBiIoSYCCEmQoiJEGIihJgIISZCiIkQYiKEmAghJkKIiRBiIoSYCCEmQoiJEGIihJgIISZCiIkQYiKEmAghJkKIiRBiIoSYCCEmQoiJEGIihJgIISZCiIkQYiKEmAghJkJ+gnVd60t4ngj5CbZtW9d10hRFyH/Wdblcxuc/v1vbYy71bdtOKdYX8rC5I5xr4nNd7UQuBzvjlvh3fQFPOk35fOfbtq2+os9MdLXbtqzrMvAF/uHqPE9vjj/qs/kifDfc8Se+rutEV3vLaFvLlzM8j3r8OU8W4a2ZjjnxWwtlzKs9u7oZXr7ZBnk51S9nOMXpY5oI7xnlOBOf7WpnOn9ejuueGf77roE/yQkifGiljnDeu3+Ly6/2tKd9/JdPm+FQvjxWXH3v5cfd/Gxro0f43JmtWtzP/YvJ1Y66IK+481jx9Ueet8RlrM980MeSZcdFedQ5ZJdnvAMeFMdbhJ95YiB3rZyRpjDiTrjznnDAOWS/C37pg+JIC+9rb29PzmG6XXG4nfCFW8ErJv6yr+K+Kb50se1+1Djl9+vXHn/pPRdXpzhQhAc9FO018UO+cjsdcV++wPYaxp75nd15cd23T0eJ8OgXzb6zao69cX7n3nT8N3t+/16fS+gl+V0a+CWKPsLy5YRHc+rOLU9MqfphgEdzenl+Z/Wx85YywkFeqr73HjnArfTOiY0w2DvTent7cud83ngpZhEO+0Nb4/tkdCPkN4cBbqlnQQkWyvddnaH72mOG2RIP/bJNkN/lD2uNfJ3Lskz1G1Kn0+lyzLPfQz5uiYevgeMinOA+/e7rMdKJ5RPjD/bywS94CHxIsQaO+836wRfKvOYa7NAFRka/iR5qzp1wCuMeR98p1oAIL4jw9RxHP5r7P3piCudtkKtECDHH0T9N9RLFRKZ5Jlx+9EsUwFWOoxATIcRECDERQkyEEBMhxEQIMRFCTIQQEyHERAgxEUJMhBATIcRECDERQkyEEBMhxEQIMRFCTIQQEyHERAgxEUJMhBATIcRECDERQkyEEBMhxEQIMRFCTIQQEyHERAgxEUJMhBATIcRECDERQkyEEBMhxEQIMRFCTIQQEyHERAgxEUJMhBATIcRECDERQkyEEBMhxEQIMRFCTIQQEyHERAgxEUJMhBATIcRECDERQkyEEBMhxEQIMRFCTIQQEyHERAgxEUJMhBATIcRECDERQkyEEBMhxEQIMRFCTIQQEyHERAgxEUJMhBATIcRECDERQkyEEBMhxEQIMRFCTIQQEyHERAgxEUJMhBATIcRECDERQkyEEBMhxEQIMRFCTIQQEyHERAgxEUJMhBATIcRECDERQkyEEBMhxEQIMRFCTIQQEyHERAgxEUJMhBATIcRECDERQkyEEBMhxEQIMRFCTIQQEyHERAgxEUJMhBATIcT+AfS8+aFalQMkAAAAAElFTkSuQmCC'
'''

#
@app.route("/drawMolecule",methods=['POST'])
def drawMolecule():
    #image = molecula()
    if not request.json:
        abort(400)

    '''
    format json
    {"drawMolecule":"CC(=O)Nc1ccc(O)cc1"}
    '''
    try:
        imagestr = (request.json['drawMolecule'])
    except:
        abort(400)

    image = molecula(imagestr)
    return render_template('index.html', image = image)


@app.route("/drawMolecule/<string_molecula>")
def drawMoleculeurl(string_molecula):

    image = molecula(string_molecula)
    return render_template('index.html', image = image)

# Todo: Convert image to base64
def molecula(str):
    #Todo: i don't know if is the best way yo convert to base64
    #       but is the best i can can go for now
    try:
        x = Chem.MolFromSmiles(str)
        #x = Chem.MolFromSmiles(lista[2])
    except:
        abort(400)
    else:
        image = Draw.MolToImage(x)
        buffered = BytesIO()
        image = image.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue())
        img_str = img_str.decode(encoding='utf-8')
        return img_str
