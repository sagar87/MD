import cPickle, base64
try:
	from SimpleSession.versions.v62 import beginRestore,\
	    registerAfterModelsCB, reportRestoreError, checkVersion
except ImportError:
	from chimera import UserError
	raise UserError('Cannot open session that was saved in a'
	    ' newer version of Chimera; update your version')
checkVersion([1, 10, 1, 40427])
import chimera
from chimera import replyobj
replyobj.status('Restoring session...', \
    blankAfter=0)
replyobj.status('Beginning session restore...', \
    blankAfter=0, secondary=True)
beginRestore()

def restoreCoreModels():
	from SimpleSession.versions.v62 import init, restoreViewer, \
	     restoreMolecules, restoreColors, restoreSurfaces, \
	     restoreVRML, restorePseudoBondGroups, restoreModelAssociations
	molInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVRFyaWJib25JbnNpZGVDb2xvcnECSwFOfYdVCWJhbGxTY2FsZXEDSwFHP9AAAAAAAAB9h1UJcG9pbnRTaXplcQRLAUc/8AAAAAAAAH2HVQVjb2xvcnEFSwFLAH2HVQpyaWJib25UeXBlcQZLAUsAfYdVCnN0aWNrU2NhbGVxB0sBRz/wAAAAAAAAfYdVDGFyb21hdGljTW9kZXEISwFLAX2HVQp2ZHdEZW5zaXR5cQlLAUdAFAAAAAAAAH2HVQZoaWRkZW5xCksBiX2HVQ1hcm9tYXRpY0NvbG9ycQtLAU59h1UPcmliYm9uU21vb3RoaW5ncQxLAUsAfYdVCWF1dG9jaGFpbnENSwGIfYdVCG9wdGlvbmFscQ59VQ9sb3dlckNhc2VDaGFpbnNxD0sBiX2HVQlsaW5lV2lkdGhxEEsBR0AAAAAAAAAAfYdVD3Jlc2lkdWVMYWJlbFBvc3ERSwFLAH2HVQRuYW1lcRJLAVgHAAAAc2NyYXRjaH2HVQ9hcm9tYXRpY0Rpc3BsYXlxE0sBiX2HVQ9yaWJib25TdGlmZm5lc3NxFEsBRz/pmZmZmZmafYdVCnBkYkhlYWRlcnNxFV1xFn1xF2FVA2lkc3EYSwFLAEsAhn2HVQ5zdXJmYWNlT3BhY2l0eXEZSwFHv/AAAAAAAAB9h1UQYXJvbWF0aWNMaW5lVHlwZXEaSwFLAn2HVRRyaWJib25IaWRlc01haW5jaGFpbnEbSwGIfYdVB2Rpc3BsYXlxHEsBiH2HdS4='))
	resInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVQZpbnNlcnRxAksOVQEgfYdVC2ZpbGxEaXNwbGF5cQNLDol9h1UEbmFtZXEESw5YAwAAAFNFUn1xBShYAwAAAFBST11xBihLAksFSwlLDGVYAwAAAFRZUl1xByhLAEsHZVgDAAAAVEhSXXEIKEsDSwpldYdVBWNoYWlucQlLDlgBAAAAQX2HVQ5yaWJib25EcmF3TW9kZXEKSw5LAn2HVQJzc3ELSw6JiYZ9h1UIbW9sZWN1bGVxDEsOSwB9h1ULcmliYm9uQ29sb3JxDUsOSwF9cQ4oSwJOXXEPSwFLAYZxEGGGSwNOXXERSwJLAYZxEmGGSwROXXETSwNLAYZxFGGGSwVOXXEVSwRLAYZxFmGGSwZOXXEXSwVLAYZxGGGGSwdOXXEZSwZLAYZxGmGGSwhOXXEbSwdLAYZxHGGGSwlOXXEdSwhLAYZxHmGGSwpOXXEfSwlLAYZxIGGGSwtOXXEhSwpLAYZxImGGSwxOXXEjSwtLAYZxJGGGSw1OXXElSwxLAYZxJmGGSw5OXXEnSw1LAYZxKGGGdYdVBWxhYmVscSlLDlgAAAAAfYdVCmxhYmVsQ29sb3JxKksOTn2HVQhmaWxsTW9kZXErSw5LAX2HVQVpc0hldHEsSw6JfYdVC2xhYmVsT2Zmc2V0cS1LDk59h1UIcG9zaXRpb25xLl1xL0sBSw6GcTBhVQ1yaWJib25EaXNwbGF5cTFLDol9h1UIb3B0aW9uYWxxMn1VBHNzSWRxM0sOSv////99h3Uu'))
	atomInfo = cPickle.loads(base64.b64decode('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'))
	bondInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVQVjb2xvcnECS85OfYdVBWF0b21zcQNdcQQoXXEFKEsQSw9lXXEGKEsRSxBlXXEHKEsSSxFlXXEIKEsTSxFlXXEJKEsUSxNlXXEKKEsVSxRlXXELKEsWSxVlXXEMKEsXSxVlXXENKEsYSxdlXXEOKEsZSxhlXXEPKEsaSxllXXEQKEsbSxllXXERKEscSxtlXXESKEsdSxxlXXETKEseSx1lXXEUKEsfSx1lXXEVKEsgSx9lXXEWKEshSyBlXXEXKEsiSyFlXXEYKEsjSyFlXXEZKEskSyNlXXEaKEslSyRlXXEbKEsmSyVlXXEcKEsnSyVlXXEdKEsoSydlXXEeKEspSyhlXXEfKEsqSyllXXEgKEsrSyllXXEhKEssSytlXXEiKEstSyxlXXEjKEsuSy1lXXEkKEsvSy1lXXElKEswSy9lXXEmKEsxSzBlXXEnKEsySzFlXXEoKEszSzFlXXEpKEs0SzNlXXEqKEs1SzRlXXErKEs2SzVlXXEsKEs3SzVlXXEtKEs4SzdlXXEuKEs5SzhlXXEvKEs6SzllXXEwKEs7SzllXXExKEs8SztlXXEyKEs9SzxlXXEzKEs+Sz1lXXE0KEs/Sz1lXXE1KEtASz9lXXE2KEtBS0BlXXE3KEtCS0FlXXE4KEtDS0FlXXE5KEtES0NlXXE6KEtFS0RlXXE7KEtGS0VlXXE8KEtHS0VlXXE9KEtISxBlXXE+KEtJS0hlXXE/KEtKS0llXXFAKEtLS0llXXFBKEtMS0tlXXFCKEtNS0xlXXFDKEtOS01lXXFEKEtPS01lXXFFKEtOS0plXXFGKEtQSxRlXXFHKEtRS1BlXXFIKEtSSxhlXXFJKEtTS1JlXXFKKEtUS1NlXXFLKEtUSxdlXXFMKEtVSxxlXXFNKEtWS1VlXXFOKEtXS1VlXXFPKEtYSyBlXXFQKEtZS1hlXXFRKEtaSyRlXXFSKEtbS1plXXFTKEtcS1tlXXFUKEtcSyNlXXFVKEtdSyhlXXFWKEteS11lXXFXKEtfSyxlXXFYKEtgS19lXXFZKEthS2BlXXFaKEtiS2BlXXFbKEtjS2JlXXFcKEtkS2NlXXFdKEtlS2RlXXFeKEtmS2RlXXFfKEtmS2FlXXFgKEtnSzBlXXFhKEtoS2dlXXFiKEtpSzRlXXFjKEtqS2llXXFkKEtrS2plXXFlKEtrSzNlXXFmKEtsSzhlXXFnKEttS2xlXXFoKEtuS2xlXXFpKEtvSzxlXXFqKEtwS29lXXFrKEtxS0BlXXFsKEtyS3FlXXFtKEtzS3JlXXFuKEtzSz9lXXFvKEt0S0RlXXFwKEt1S3RlXXFxKEt2SxBlXXFyKEt3SxNlXXFzKEt4SxRlXXF0KEt5SxhlXXF1KEt6SxtlXXF2KEt7SxxlXXF3KEt8Sx9lXXF4KEt9SyBlXXF5KEt+SyRlXXF6KEt/SydlXXF7KEuASyhlXXF8KEuBSytlXXF9KEuCSyxlXXF+KEuDSy9lXXF/KEuESzBlXXGAKEuFSzRlXXGBKEuGSzdlXXGCKEuHSzhlXXGDKEuISztlXXGEKEuJSzxlXXGFKEuKS0BlXXGGKEuLS0NlXXGHKEuMS0RlXXGIKEuNS0hlXXGJKEuOS0hlXXGKKEuPS0plXXGLKEuQS0tlXXGMKEuRS0xlXXGNKEuSS05lXXGOKEuTS1BlXXGPKEuUS1BlXXGQKEuVS1JlXXGRKEuWS1JlXXGSKEuXS1NlXXGTKEuYS1NlXXGUKEuZS1RlXXGVKEuaS1RlXXGWKEubS1VlXXGXKEucS1hlXXGYKEudS1hlXXGZKEueS1plXXGaKEufS1plXXGbKEugS1tlXXGcKEuhS1tlXXGdKEuiS1xlXXGeKEujS1xlXXGfKEukS11lXXGgKEulS11lXXGhKEumS19lXXGiKEunS19lXXGjKEuoS2FlXXGkKEupS2JlXXGlKEuqS2NlXXGmKEurS2ZlXXGnKEusS2dlXXGoKEutS2dlXXGpKEuuS2llXXGqKEuvS2llXXGrKEuwS2plXXGsKEuxS2plXXGtKEuyS2tlXXGuKEuzS2tlXXGvKEu0S2xlXXGwKEu1S29lXXGxKEu2S29lXXGyKEu3S3FlXXGzKEu4S3FlXXG0KEu5S3JlXXG1KEu6S3JlXXG2KEu7S3NlXXG3KEu8S3NlXXG4KEu9S3RlXXG5KEu+S3RlXXG6KEu/S21lXXG7KEvAS25lXXG8KEvBS25lXXG9KEvCS25lXXG+KEvDS1ZlXXG/KEvES3BlXXHAKEvFS1dlXXHBKEvGS1dlXXHCKEvHS1dlXXHDKEvIS1llXXHEKEvJSw9lXXHFKEvKSw9lXXHGKEvLSw9lXXHHKEvMS3VlXXHIKEvNS15lXXHJKEvOS2VlXXHKKEvPS2hlXXHLKEvQS09lXXHMKEvRS1FlXXHNKEvSS9FlXXHOKEvTS9FlXXHPKEvUS9FlXXHQKEvVS89lXXHRKEvWS89lXXHSKEvXS89lZVUFbGFiZWxx00vOWAAAAAB9h1UIaGFsZmJvbmRx1EvOiH2HVQZyYWRpdXNx1UvORz/JmZmgAAAAfYdVC2xhYmVsT2Zmc2V0cdZLzk59h1UIZHJhd01vZGVx10vOSwB9h1UIb3B0aW9uYWxx2H1VB2Rpc3BsYXlx2UvOSwJ9h3Uu'))
	crdInfo = cPickle.loads(base64.b64decode('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'))
	surfInfo = {'category': (0, None, {}), 'probeRadius': (0, None, {}), 'pointSize': (0, None, {}), 'name': [], 'density': (0, None, {}), 'colorMode': (0, None, {}), 'useLighting': (0, None, {}), 'transparencyBlendMode': (0, None, {}), 'molecule': [], 'smoothLines': (0, None, {}), 'lineWidth': (0, None, {}), 'allComponents': (0, None, {}), 'twoSidedLighting': (0, None, {}), 'customVisibility': [], 'drawMode': (0, None, {}), 'display': (0, None, {}), 'customColors': []}
	vrmlInfo = {'subid': (0, None, {}), 'display': (0, None, {}), 'id': (0, None, {}), 'vrmlString': [], 'name': (0, None, {})}
	colors = {'Ru': ((0.141176, 0.560784, 0.560784), 1, u'default'), 'firebrick': ((0.698039, 0.133333, 0.133333), 1, u'default'), 'Re': ((0.14902, 0.490196, 0.670588), 1, u'default'), 'Rf': ((0.8, 0, 0.34902), 1, u'default'), 'Ra': ((0, 0.490196, 0), 1, u'default'), 'Rb': ((0.439216, 0.180392, 0.690196), 1, u'default'), 'Rn': ((0.258824, 0.509804, 0.588235), 1, u'default'), 'Rh': ((0.0392157, 0.490196, 0.54902), 1, u'default'), 'Be': ((0.760784, 1, 0), 1, u'default'), 'Ba': ((0, 0.788235, 0), 1, u'default'), 'Bh': ((0.878431, 0, 0.219608), 1, u'default'), 'Bi': ((0.619608, 0.309804, 0.709804), 1, u'default'), 'Bk': ((0.541176, 0.309804, 0.890196), 1, u'default'), 'Br': ((0.65098, 0.160784, 0.160784), 1, u'default'), 'H': ((1, 1, 1), 1, u'default'), 'Dy': ((0.121569, 1, 0.780392), 1, u'default'), 'P': ((1, 0.501961, 0), 1, u'default'), 'Os': ((0.14902, 0.4, 0.588235), 1, u'default'), 'Ge': ((0.4, 0.560784, 0.560784), 1, u'default'), 'Gd': ((0.270588, 1, 0.780392), 1, u'default'), 'Ga': ((0.760784, 0.560784, 0.560784), 1, u'default'), 'Pr': ((0.85098, 1, 0.780392), 1, u'default'),
'Pt': ((0.815686, 0.815686, 0.878431), 1, u'default'), 'Pu': ((0, 0.419608, 1), 1, u'default'), 'C': ((0.564706, 0.564706, 0.564706), 1, u'default'), 'Pb': ((0.341176, 0.34902, 0.380392), 1, u'default'), 'Pa': ((0, 0.631373, 1), 1, u'default'), 'Pd': ((0, 0.411765, 0.521569), 1, u'default'), 'Cd': ((1, 0.85098, 0.560784), 1, u'default'), 'Po': ((0.670588, 0.360784, 0), 1, u'default'), 'Pm': ((0.639216, 1, 0.780392), 1, u'default'), 'Hs': ((0.901961, 0, 0.180392), 1, u'default'), 'Ho': ((0, 1, 0.611765), 1, u'default'), 'Hf': ((0.301961, 0.760784, 1), 1, u'default'), 'Hg': ((0.721569, 0.721569, 0.815686), 1, u'default'), 'He': ((0.85098, 1, 1), 1, u'default'), 'Md': ((0.701961, 0.0509804, 0.65098), 1, u'default'), 'Mg': ((0.541176, 1, 0), 1, u'default'), 'K': ((0.560784, 0.25098, 0.831373), 1, u'default'), 'Mn': ((0.611765, 0.478431, 0.780392), 1, u'default'), 'O': ((1, 0.0509804, 0.0509804), 1, u'default'), 'Mt': ((0.921569, 0, 0.14902), 1, u'default'), 'S': ((1, 1, 0.188235), 1, u'default'), 'W': ((0.129412, 0.580392, 0.839216), 1, u'default'), 'Zn': ((0.490196, 0.501961, 0.690196), 1, u'default'),
'Eu': ((0.380392, 1, 0.780392), 1, u'default'), 'Zr': ((0.580392, 0.878431, 0.878431), 1, u'default'), 'Er': ((0, 0.901961, 0.458824), 1, u'default'), 'Ni': ((0.313725, 0.815686, 0.313725), 1, u'default'), 'No': ((0.741176, 0.0509804, 0.529412), 1, u'default'), 'Na': ((0.670588, 0.360784, 0.94902), 1, u'default'), 'Nb': ((0.45098, 0.760784, 0.788235), 1, u'default'), 'Nd': ((0.780392, 1, 0.780392), 1, u'default'), 'Ne': ((0.701961, 0.890196, 0.960784), 1, u'default'), 'Np': ((0, 0.501961, 1), 1, u'default'), 'Fr': ((0.258824, 0, 0.4), 1, u'default'), 'Fe': ((0.878431, 0.4, 0.2), 1, u'default'), 'Fm': ((0.701961, 0.121569, 0.729412), 1, u'default'), 'B': ((1, 0.709804, 0.709804), 1, u'default'), 'F': ((0.564706, 0.878431, 0.313725), 1, u'default'), 'Sr': ((0, 1, 0), 1, u'default'), 'N': ((0.188235, 0.313725, 0.972549), 1, u'default'), 'Kr': ((0.360784, 0.721569, 0.819608), 1, u'default'), 'Si': ((0.941176, 0.784314, 0.627451), 1, u'default'), 'Sn': ((0.4, 0.501961, 0.501961), 1, u'default'), 'Sm': ((0.560784, 1, 0.780392), 1, u'default'), 'V': ((0.65098, 0.65098, 0.670588), 1, u'default'),
'Sc': ((0.901961, 0.901961, 0.901961), 1, u'default'), 'Sb': ((0.619608, 0.388235, 0.709804), 1, u'default'), 'Sg': ((0.85098, 0, 0.270588), 1, u'default'), 'Se': ((1, 0.631373, 0), 1, u'default'), 'Co': ((0.941176, 0.564706, 0.627451), 1, u'default'), 'Cm': ((0.470588, 0.360784, 0.890196), 1, u'default'), 'Cl': ((0.121569, 0.941176, 0.121569), 1, u'default'), 'Ca': ((0.239216, 1, 0), 1, u'default'), 'Cf': ((0.631373, 0.211765, 0.831373), 1, u'default'), 'Ce': ((1, 1, 0.780392), 1, u'default'), 'Xe': ((0.258824, 0.619608, 0.690196), 1, u'default'), 'Tm': ((0, 0.831373, 0.321569), 1, u'default'), 'Cs': ((0.341176, 0.0901961, 0.560784), 1, u'default'), 'Cr': ((0.541176, 0.6, 0.780392), 1, u'default'), 'Cu': ((0.784314, 0.501961, 0.2), 1, u'default'), 'La': ((0.439216, 0.831373, 1), 1, u'default'), 'Li': ((0.8, 0.501961, 1), 1, u'default'), 'Tl': ((0.65098, 0.329412, 0.301961), 1, u'default'), 'Lu': ((0, 0.670588, 0.141176), 1, u'default'), 'Lr': ((0.780392, 0, 0.4), 1, u'default'), 'Th': ((0, 0.729412, 1), 1, u'default'), 'Ti': ((0.74902, 0.760784, 0.780392), 1, u'default'),
'tan': ((0.823529, 0.705882, 0.54902), 1, u'default'), 'Te': ((0.831373, 0.478431, 0), 1, u'default'), 'Tb': ((0.188235, 1, 0.780392), 1, u'default'), 'Tc': ((0.231373, 0.619608, 0.619608), 1, u'default'), 'Ta': ((0.301961, 0.65098, 1), 1, u'default'), 'Yb': ((0, 0.74902, 0.219608), 1, u'default'), 'Db': ((0.819608, 0, 0.309804), 1, u'default'), 'navy blue': ((0, 0, 0.501961), 1, u'default'), 'At': ((0.458824, 0.309804, 0.270588), 1, u'default'), 'I': ((0.580392, 0, 0.580392), 1, u'default'), 'U': ((0, 0.560784, 1), 1, u'default'), 'Y': ((0.580392, 1, 1), 1, u'default'), 'Ac': ((0.439216, 0.670588, 0.980392), 1, u'default'), 'Ag': ((0.752941, 0.752941, 0.752941), 1, u'default'), 'Ir': ((0.0901961, 0.329412, 0.529412), 1, u'default'), 'Am': ((0.329412, 0.360784, 0.94902), 1, u'default'), 'Al': ((0.74902, 0.65098, 0.65098), 1, u'default'), 'As': ((0.741176, 0.501961, 0.890196), 1, u'default'), 'Ar': ((0.501961, 0.819608, 0.890196), 1, u'default'), 'Au': ((1, 0.819608, 0.137255), 1, u'default'), 'Es': ((0.701961, 0.121569, 0.831373), 1, u'default'), 'In': ((0.65098, 0.458824, 0.45098), 1, u'default'),
'Mo': ((0.329412, 0.709804, 0.709804), 1, u'default')}
	materials = {u'default': ((1, 1, 1), 30)}
	pbInfo = {'category': [u'distance monitor'], 'bondInfo': [{'color': (0, None, {}), 'atoms': [], 'label': (0, None, {}), 'halfbond': (0, None, {}), 'labelColor': (0, None, {}), 'drawMode': (0, None, {}), 'display': (0, None, {})}], 'lineType': (1, 2, {}), 'color': (1, 20, {}), 'optional': {'fixedLabels': (True, False, (1, False, {}))}, 'display': (1, True, {}), 'showStubBonds': (1, False, {}), 'lineWidth': (1, 1, {}), 'stickScale': (1, 1, {}), 'id': [-2]}
	modelAssociations = {}
	colorInfo = (23, (u'', (0, 0.923077, 1, 1)), {(u'', (1, 0.307692, 0, 1)): [13], (u'tan', (0.823529, 0.705882, 0.54902, 1)): [0], (u'', (1, 0.923077, 0, 1)): [11], (u'red', (1, 0, 0, 1)): [14], (u'', (0, 1, 0.461538, 1)): [6], (u'H', (1, 1, 1, 1)): [17], (u'', (1, 0.615385, 0, 1)): [12], (u'N', (0.188235, 0.313725, 0.972549, 1)): [15], (u'P', (1, 0.501961, 0, 1)): [18], (u'black', (0, 0, 0, 1)): [21], (u'', (0.769231, 1, 0, 1)): [10], (u'', (0, 0.307692, 1, 1)): [2], (u'O', (1, 0.0509804, 0.0509804, 1)): [16], (u'', (0, 1, 0.153846, 1)): [7], (u'yellow', (1, 1, 0, 1)): [20], (u'', (0, 0.615385, 1, 1)): [3], (u'', (0.153846, 1, 0, 1)): [8], (u'C', (0.564706, 0.564706, 0.564706, 1)): [19], (u'', (0.461538, 1, 0, 1)): [9], (u'green', (0, 1, 0, 1)): [22], (u'', (0, 1, 0.769231, 1)): [5], (u'blue', (0, 0, 1, 1)): [1]})
	viewerInfo = {'cameraAttrs': {'center': (-8.7315887561706, -3.6708787472028, -2.0187671634638), 'fieldOfView': 20.425371539944, 'nearFar': (27.932447742849, -17.762646032315), 'ortho': False, 'eyeSeparation': 50.8, 'focal': 4.9005750977789}, 'viewerAttrs': {'silhouetteColor': None, 'clipping': False, 'showSilhouette': False, 'showShadows': False, 'viewSize': 17.386321014272, 'labelsOnTop': True, 'depthCueRange': (0.5, 1), 'silhouetteWidth': 2, 'singleLayerTransparency': True, 'shadowTextureSize': 2048, 'backgroundImage': [None, 1, 2, 1, 0, 0], 'backgroundGradient': [('Chimera default', [(1, 1, 1, 1), (0, 0, 1, 1)], 1), 1, 0, 0], 'depthCue': True, 'highlight': 0, 'scaleFactor': 0.78197595741275, 'angleDependentTransparency': True, 'backgroundMethod': 0}, 'viewerHL': 22, 'cameraMode': 'mono', 'detail': 1.5, 'viewerFog': None, 'viewerBG': 21}

	replyobj.status("Initializing session restore...", blankAfter=0,
		secondary=True)
	from SimpleSession.versions.v62 import expandSummary
	init(dict(enumerate(expandSummary(colorInfo))))
	replyobj.status("Restoring colors...", blankAfter=0,
		secondary=True)
	restoreColors(colors, materials)
	replyobj.status("Restoring molecules...", blankAfter=0,
		secondary=True)
	restoreMolecules(molInfo, resInfo, atomInfo, bondInfo, crdInfo)
	replyobj.status("Restoring surfaces...", blankAfter=0,
		secondary=True)
	restoreSurfaces(surfInfo)
	replyobj.status("Restoring VRML models...", blankAfter=0,
		secondary=True)
	restoreVRML(vrmlInfo)
	replyobj.status("Restoring pseudobond groups...", blankAfter=0,
		secondary=True)
	restorePseudoBondGroups(pbInfo)
	replyobj.status("Restoring model associations...", blankAfter=0,
		secondary=True)
	restoreModelAssociations(modelAssociations)
	replyobj.status("Restoring camera...", blankAfter=0,
		secondary=True)
	restoreViewer(viewerInfo)

try:
	restoreCoreModels()
except:
	reportRestoreError("Error restoring core models")

	replyobj.status("Restoring extension info...", blankAfter=0,
		secondary=True)


try:
	import StructMeasure
	from StructMeasure.DistMonitor import restoreDistances
	registerAfterModelsCB(restoreDistances, 1)
except:
	reportRestoreError("Error restoring distances in session")


def restoreMidasBase():
	formattedPositions = {'session-start': (1.9666095722079, 17.386321014272, (-8.7315887561706, -3.6708787472028, -2.0187671634638), (24.696655624293, -20.955385414504), 4.9005750977789, {(0, 0): ((-15.106797080346, -4.7890383654637, -0.95044757630367), (0.009513766589673813, 0.9132402527600205, -0.4073103595344602, 59.78057354582901))}, {(0, 0, 'Molecule'): (False, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, False, 5.0)}, 0, (-8.73159, -3.67088, -2.01877), False, 20.425371539944)}
	import Midas
	Midas.restoreMidasBase(formattedPositions)
try:
	restoreMidasBase()
except:
	reportRestoreError('Error restoring Midas base state')


def restoreMidasText():
	from Midas import midas_text
	midas_text.aliases = {}
	midas_text.userSurfCategories = {}

try:
	restoreMidasText()
except:
	reportRestoreError('Error restoring Midas text state')

geomData = {'AxisManager': {}, 'CentroidManager': {}, 'PlaneManager': {}}

try:
	from StructMeasure.Geometry import geomManager
	geomManager._restoreSession(geomData)
except:
	reportRestoreError("Error restoring geometry objects in session")


def restoreSession_RibbonStyleEditor():
	import SimpleSession
	import RibbonStyleEditor
	userScalings = []
	userXSections = []
	userResidueClasses = []
	residueData = [(1, 'Chimera default', 'rounded', u'amino acid'), (2, 'Chimera default', 'rounded', u'amino acid'), (3, 'Chimera default', 'rounded', u'amino acid'), (4, 'Chimera default', 'rounded', u'amino acid'), (5, 'Chimera default', 'rounded', u'amino acid'), (6, 'Chimera default', 'rounded', u'amino acid'), (7, 'Chimera default', 'rounded', u'amino acid'), (8, 'Chimera default', 'rounded', u'amino acid'), (9, 'Chimera default', 'rounded', u'amino acid'), (10, 'Chimera default', 'rounded', u'amino acid'), (11, 'Chimera default', 'rounded', u'amino acid'), (12, 'Chimera default', 'rounded', u'amino acid'), (13, 'Chimera default', 'rounded', u'amino acid'), (14, 'Chimera default', 'rounded', u'amino acid')]
	flags = RibbonStyleEditor.NucleicDefault1
	SimpleSession.registerAfterModelsCB(RibbonStyleEditor.restoreState,
				(userScalings, userXSections,
				userResidueClasses, residueData, flags))
try:
	restoreSession_RibbonStyleEditor()
except:
	reportRestoreError("Error restoring RibbonStyleEditor state")

trPickle = 'gAJjQW5pbWF0ZS5UcmFuc2l0aW9ucwpUcmFuc2l0aW9ucwpxASmBcQJ9cQMoVQxjdXN0b21fc2NlbmVxBGNBbmltYXRlLlRyYW5zaXRpb24KVHJhbnNpdGlvbgpxBSmBcQZ9cQcoVQZmcmFtZXNxCEsBVQ1kaXNjcmV0ZUZyYW1lcQlLAVUKcHJvcGVydGllc3EKXXELVQNhbGxxDGFVBG5hbWVxDVUMY3VzdG9tX3NjZW5lcQ5VBG1vZGVxD1UGbGluZWFycRB1YlUIa2V5ZnJhbWVxEWgFKYFxEn1xEyhoCEsUaAlLAWgKXXEUaAxhaA1VCGtleWZyYW1lcRVoD2gQdWJVBXNjZW5lcRZoBSmBcRd9cRgoaAhLAWgJSwFoCl1xGWgMYWgNVQVzY2VuZXEaaA9oEHVidWIu'
scPickle = 'gAJjQW5pbWF0ZS5TY2VuZXMKU2NlbmVzCnEBKYFxAn1xA1UHbWFwX2lkc3EEfXNiLg=='
kfPickle = 'gAJjQW5pbWF0ZS5LZXlmcmFtZXMKS2V5ZnJhbWVzCnEBKYFxAn1xA1UHZW50cmllc3EEXXEFc2Iu'
def restoreAnimation():
	'A method to unpickle and restore animation objects'
	# Scenes must be unpickled after restoring transitions, because each
	# scene links to a 'scene' transition. Likewise, keyframes must be 
	# unpickled after restoring scenes, because each keyframe links to a scene.
	# The unpickle process is left to the restore* functions, it's 
	# important that it doesn't happen prior to calling those functions.
	import SimpleSession
	from Animate.Session import restoreTransitions
	from Animate.Session import restoreScenes
	from Animate.Session import restoreKeyframes
	SimpleSession.registerAfterModelsCB(restoreTransitions, trPickle)
	SimpleSession.registerAfterModelsCB(restoreScenes, scPickle)
	SimpleSession.registerAfterModelsCB(restoreKeyframes, kfPickle)
try:
	restoreAnimation()
except:
	reportRestoreError('Error in Animate.Session')

def restoreLightController():
	import Lighting
	Lighting._setFromParams({'ratio': 1.25, 'brightness': 1.16, 'material': [30.0, (1.0, 1.0, 1.0), 1], 'back': [(0.3574067443365933, 0.6604015517481455, -0.6604015517481456), (1.0, 1.0, 1.0), 0.0], 'mode': 'two-point', 'key': [(-0.3574067443365933, 0.6604015517481455, 0.6604015517481456), (1.0, 1.0, 1.0), 1.0], 'contrast': 0.83, 'fill': [(0.2505628070857316, 0.2505628070857316, 0.9351131265310294), (1.0, 1.0, 1.0), 0.0]})
try:
	restoreLightController()
except:
	reportRestoreError("Error restoring lighting parameters")


try:
	from BuildStructure.gui import _sessionRestore
	_sessionRestore({'mapped': 0})
except:
	reportRestoreError("Failure restoring Build Structure")


def restoreRemainder():
	from SimpleSession.versions.v62 import restoreWindowSize, \
	     restoreOpenStates, restoreSelections, restoreFontInfo, \
	     restoreOpenModelsAttrs, restoreModelClip, restoreSilhouettes

	curSelIds =  [213]
	savedSels = []
	openModelsAttrs = { 'cofrMethod': 0 }
	from chimera import Point
	openModelsAttrs['cofr'] = Point(-9.8889, -5.04882, -2.01877)
	windowSize = (1920, 1106)
	xformMap = {0: (((-0.038661285093368, 0.92687042958281, -0.37338520565216), 104.44065596989), (-13.910735345674, -4.7818186053788, 3.1569804929716), True)}
	fontInfo = {'face': ('Sans Serif', 'Normal', 16)}
	clipPlaneInfo = {}
	silhouettes = {0: True, 422: True}

	replyobj.status("Restoring window...", blankAfter=0,
		secondary=True)
	restoreWindowSize(windowSize)
	replyobj.status("Restoring open states...", blankAfter=0,
		secondary=True)
	restoreOpenStates(xformMap)
	replyobj.status("Restoring font info...", blankAfter=0,
		secondary=True)
	restoreFontInfo(fontInfo)
	replyobj.status("Restoring selections...", blankAfter=0,
		secondary=True)
	restoreSelections(curSelIds, savedSels)
	replyobj.status("Restoring openModel attributes...", blankAfter=0,
		secondary=True)
	restoreOpenModelsAttrs(openModelsAttrs)
	replyobj.status("Restoring model clipping...", blankAfter=0,
		secondary=True)
	restoreModelClip(clipPlaneInfo)
	replyobj.status("Restoring per-model silhouettes...", blankAfter=0,
		secondary=True)
	restoreSilhouettes(silhouettes)

	replyobj.status("Restoring remaining extension info...", blankAfter=0,
		secondary=True)
try:
	restoreRemainder()
except:
	reportRestoreError("Error restoring post-model state")
from SimpleSession.versions.v62 import makeAfterModelsCBs
makeAfterModelsCBs()

from SimpleSession.versions.v62 import endRestore
replyobj.status('Finishing restore...', blankAfter=0, secondary=True)
endRestore({})
replyobj.status('', secondary=True)
replyobj.status('Restore finished.')

