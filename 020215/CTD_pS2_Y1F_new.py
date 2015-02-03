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
	resInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVQZpbnNlcnRxAksOVQEgfYdVC2ZpbGxEaXNwbGF5cQNLDol9h1UEbmFtZXEESw5YAwAAAFNFUn1xBShYAwAAAFBST11xBihLAksFSwlLDGVYAwAAAFZBTF1xByhLA0sKZVgDAAAAUEhFXXEIKEsASwdldYdVBWNoYWlucQlLDlgBAAAAQX2HVQ5yaWJib25EcmF3TW9kZXEKSw5LAn2HVQJzc3ELSw6JiYZ9h1UIbW9sZWN1bGVxDEsOSwB9h1ULcmliYm9uQ29sb3JxDUsOSwF9cQ4oSwJOXXEPSwFLAYZxEGGGSwNOXXERSwJLAYZxEmGGSwROXXETSwNLAYZxFGGGSwVOXXEVSwRLAYZxFmGGSwZOXXEXSwVLAYZxGGGGSwdOXXEZSwZLAYZxGmGGSwhOXXEbSwdLAYZxHGGGSwlOXXEdSwhLAYZxHmGGSwpOXXEfSwlLAYZxIGGGSwtOXXEhSwpLAYZxImGGSwxOXXEjSwtLAYZxJGGGSw1OXXElSwxLAYZxJmGGSw5OXXEnSw1LAYZxKGGGdYdVBWxhYmVscSlLDlgAAAAAfYdVCmxhYmVsQ29sb3JxKksOTn2HVQhmaWxsTW9kZXErSw5LAX2HVQVpc0hldHEsSw6JfYdVC2xhYmVsT2Zmc2V0cS1LDk59h1UIcG9zaXRpb25xLl1xL0sBSw6GcTBhVQ1yaWJib25EaXNwbGF5cTFLDol9h1UIb3B0aW9uYWxxMn1VBHNzSWRxM0sOSv////99h3Uu'))
	atomInfo = cPickle.loads(base64.b64decode('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'))
	bondInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVQVjb2xvcnECS9BOfYdVBWF0b21zcQNdcQQoXXEFKEsQSw9lXXEGKEsRSxBlXXEHKEsSSxFlXXEIKEsTSxFlXXEJKEsUSxNlXXEKKEsVSxRlXXELKEsWSxVlXXEMKEsXSxVlXXENKEsYSxdlXXEOKEsZSxhlXXEPKEsaSxllXXEQKEsbSxllXXERKEscSxtlXXESKEsdSxxlXXETKEseSx1lXXEUKEsfSx1lXXEVKEsgSx9lXXEWKEshSyBlXXEXKEsiSyFlXXEYKEsjSyFlXXEZKEskSyNlXXEaKEslSyRlXXEbKEsmSyVlXXEcKEsnSyVlXXEdKEsoSydlXXEeKEspSyhlXXEfKEsqSyllXXEgKEsrSyllXXEhKEssSytlXXEiKEstSyxlXXEjKEsuSy1lXXEkKEsvSy1lXXElKEswSy9lXXEmKEsxSzBlXXEnKEsySzFlXXEoKEszSzFlXXEpKEs0SzNlXXEqKEs1SzRlXXErKEs2SzVlXXEsKEs3SzVlXXEtKEs4SzdlXXEuKEs5SzhlXXEvKEs6SzllXXEwKEs7SzllXXExKEs8SztlXXEyKEs9SzxlXXEzKEs+Sz1lXXE0KEs/Sz1lXXE1KEtASz9lXXE2KEtBS0BlXXE3KEtCS0FlXXE4KEtDS0FlXXE5KEtES0NlXXE6KEtFS0RlXXE7KEtGS0VlXXE8KEtHS0VlXXE9KEtISxBlXXE+KEtJS0hlXXE/KEtKS0llXXFAKEtLS0llXXFBKEtMS0tlXXFCKEtNS0xlXXFDKEtOS01lXXFEKEtOS0plXXFFKEtPSxRlXXFGKEtQS09lXXFHKEtRSxhlXXFIKEtSS1FlXXFJKEtTS1JlXXFKKEtTSxdlXXFLKEtUSxxlXXFMKEtVS1RlXXFNKEtWS1RlXXFOKEtXSyBlXXFPKEtYS1dlXXFQKEtZSyRlXXFRKEtaS1llXXFSKEtbS1plXXFTKEtbSyNlXXFUKEtcSyhlXXFVKEtdS1xlXXFWKEteSyxlXXFXKEtfS15lXXFYKEtgS19lXXFZKEthS19lXXFaKEtiS2FlXXFbKEtjS2JlXXFcKEtkS2NlXXFdKEtkS2BlXXFeKEtlSzBlXXFfKEtmS2VlXXFgKEtnSzRlXXFhKEtoS2dlXXFiKEtpS2hlXXFjKEtpSzNlXXFkKEtqSzhlXXFlKEtrS2plXXFmKEtsS2plXXFnKEttSzxlXXFoKEtuS21lXXFpKEtvS0BlXXFqKEtwS29lXXFrKEtxS3BlXXFsKEtxSz9lXXFtKEtyS0RlXXFuKEtzS3JlXXFvKEt0SxBlXXFwKEt1SxNlXXFxKEt2SxRlXXFyKEt3SxhlXXFzKEt4SxtlXXF0KEt5SxxlXXF1KEt6Sx9lXXF2KEt7SyBlXXF3KEt8SyRlXXF4KEt9SydlXXF5KEt+SyhlXXF6KEt/SytlXXF7KEuASyxlXXF8KEuBSy9lXXF9KEuCSzBlXXF+KEuDSzRlXXF/KEuESzdlXXGAKEuFSzhlXXGBKEuGSztlXXGCKEuHSzxlXXGDKEuIS0BlXXGEKEuJS0NlXXGFKEuKS0RlXXGGKEuLS0hlXXGHKEuMS0hlXXGIKEuNS0plXXGJKEuOS0tlXXGKKEuPS0xlXXGLKEuQS01lXXGMKEuRS05lXXGNKEuSS09lXXGOKEuTS09lXXGPKEuUS1FlXXGQKEuVS1FlXXGRKEuWS1JlXXGSKEuXS1JlXXGTKEuYS1NlXXGUKEuZS1NlXXGVKEuaS1RlXXGWKEubS1dlXXGXKEucS1dlXXGYKEudS1llXXGZKEueS1llXXGaKEufS1plXXGbKEugS1plXXGcKEuhS1tlXXGdKEuiS1tlXXGeKEujS1xlXXGfKEukS1xlXXGgKEulS15lXXGhKEumS15lXXGiKEunS2BlXXGjKEuoS2FlXXGkKEupS2JlXXGlKEuqS2NlXXGmKEurS2RlXXGnKEusS2VlXXGoKEutS2VlXXGpKEuuS2dlXXGqKEuvS2dlXXGrKEuwS2hlXXGsKEuxS2hlXXGtKEuyS2llXXGuKEuzS2llXXGvKEu0S2plXXGwKEu1S21lXXGxKEu2S21lXXGyKEu3S29lXXGzKEu4S29lXXG0KEu5S3BlXXG1KEu6S3BlXXG2KEu7S3FlXXG3KEu8S3FlXXG4KEu9S3JlXXG5KEu+S3JlXXG6KEu/S25lXXG7KEvAS1VlXXG8KEvBS1VlXXG9KEvCS1VlXXG+KEvDS1ZlXXG/KEvES1ZlXXHAKEvFS1ZlXXHBKEvGS1hlXXHCKEvHS3NlXXHDKEvISw9lXXHEKEvJSw9lXXHFKEvKSw9lXXHGKEvLS1BlXXHHKEvMS2tlXXHIKEvNS2tlXXHJKEvOS2tlXXHKKEvPS2ZlXXHLKEvQS2xlXXHMKEvRS2xlXXHNKEvSS2xlXXHOKEvTS11lXXHPKEvUS8tlXXHQKEvVS8tlXXHRKEvWS8tlXXHSKEvXS89lXXHTKEvYS89lXXHUKEvZS89lZVUFbGFiZWxx1UvQWAAAAAB9h1UIaGFsZmJvbmRx1kvQiH2HVQZyYWRpdXNx10vQRz/JmZmgAAAAfYdVC2xhYmVsT2Zmc2V0cdhL0E59h1UIZHJhd01vZGVx2UvQSwB9h1UIb3B0aW9uYWxx2n1VB2Rpc3BsYXlx20vQSwJ9h3Uu'))
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
	viewerInfo = {'cameraAttrs': {'center': (-1.6445754123434, -1.6874403207658, 1.4722903001415), 'fieldOfView': 40.246463653063, 'nearFar': (24.419486659058, -21.338745508656), 'ortho': False, 'eyeSeparation': 50.8, 'focal': 2.8086079087528}, 'viewerAttrs': {'silhouetteColor': None, 'clipping': False, 'showSilhouette': False, 'showShadows': False, 'viewSize': 17.879379078267, 'labelsOnTop': True, 'depthCueRange': (0.5, 1), 'silhouetteWidth': 2, 'singleLayerTransparency': True, 'shadowTextureSize': 2048, 'backgroundImage': [None, 1, 2, 1, 0, 0], 'backgroundGradient': [('Chimera default', [(1, 1, 1, 1), (0, 0, 1, 1)], 1), 1, 0, 0], 'depthCue': True, 'highlight': 0, 'scaleFactor': 0.89151928505994, 'angleDependentTransparency': True, 'backgroundMethod': 0}, 'viewerHL': 22, 'cameraMode': 'mono', 'detail': 1.5, 'viewerFog': None, 'viewerBG': 21}

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
	formattedPositions = {'session-start': (1.0, 17.389741785199, (-1.6445754123434, -1.6874403207658, 2.8086079087528), (24.137902681392, -21.030569744024), 2.8086079087528, {(0, 0): ((-1.5205766140979, -0.022196517053217, -1.0306398745412), (0.22586606077671006, 0.7753712365977102, -0.5897321154949501, 34.93213858078099))}, {(0, 0, 'Molecule'): (False, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, False, 5.0)}, 4, (-2.6057123614565114, -1.5392978485081183, 1.5536664686841029), False, 40.246463653063)}
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

	curSelIds =  [216]
	savedSels = []
	openModelsAttrs = { 'cofrMethod': 4 }
	windowSize = (1920, 1106)
	xformMap = {0: (((0.78758813039278, 0.33103708465111, 0.51973010827746), 154.94113187685), (-3.6557854880605, -1.8338390263361, 4.5303004639927), True)}
	fontInfo = {'face': ('Sans Serif', 'Normal', 16)}
	clipPlaneInfo = {}
	silhouettes = {0: True, 426: True}

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

