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
	bondInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVQVjb2xvcnECS85OfYdVBWF0b21zcQNdcQQoXXEFKEsQSw9lXXEGKEsRSxBlXXEHKEsSSxFlXXEIKEsTSxFlXXEJKEsUSxNlXXEKKEsVSxRlXXELKEsWSxVlXXEMKEsXSxVlXXENKEsYSxdlXXEOKEsZSxhlXXEPKEsaSxllXXEQKEsbSxllXXERKEscSxtlXXESKEsdSxxlXXETKEseSx1lXXEUKEsfSx1lXXEVKEsgSx9lXXEWKEshSyBlXXEXKEsiSyFlXXEYKEsjSyFlXXEZKEskSyNlXXEaKEslSyRlXXEbKEsmSyVlXXEcKEsnSyVlXXEdKEsoSydlXXEeKEspSyhlXXEfKEsqSyllXXEgKEsrSyllXXEhKEssSytlXXEiKEstSyxlXXEjKEsuSy1lXXEkKEsvSy1lXXElKEswSy9lXXEmKEsxSzBlXXEnKEsySzFlXXEoKEszSzFlXXEpKEs0SzNlXXEqKEs1SzRlXXErKEs2SzVlXXEsKEs3SzVlXXEtKEs4SzdlXXEuKEs5SzhlXXEvKEs6SzllXXEwKEs7SzllXXExKEs8SztlXXEyKEs9SzxlXXEzKEs+Sz1lXXE0KEs/Sz1lXXE1KEtASz9lXXE2KEtBS0BlXXE3KEtCS0FlXXE4KEtDS0FlXXE5KEtES0NlXXE6KEtFS0RlXXE7KEtGS0VlXXE8KEtHS0VlXXE9KEtISxBlXXE+KEtJS0hlXXE/KEtKS0llXXFAKEtLS0llXXFBKEtMS0tlXXFCKEtNS0xlXXFDKEtOS01lXXFEKEtPS01lXXFFKEtOS0plXXFGKEtQSxRlXXFHKEtRS1BlXXFIKEtSSxhlXXFJKEtTS1JlXXFKKEtUS1NlXXFLKEtUSxdlXXFMKEtVSxxlXXFNKEtWS1VlXXFOKEtXS1VlXXFPKEtYSyBlXXFQKEtZS1hlXXFRKEtaSyRlXXFSKEtbS1plXXFTKEtcS1tlXXFUKEtcSyNlXXFVKEtdSyhlXXFWKEteS11lXXFXKEtfSyxlXXFYKEtgS19lXXFZKEthS2BlXXFaKEtiS2BlXXFbKEtjS2JlXXFcKEtkS2NlXXFdKEtlS2RlXXFeKEtmS2RlXXFfKEtmS2FlXXFgKEtnSzBlXXFhKEtoS2dlXXFiKEtpSzRlXXFjKEtqS2llXXFkKEtrS2plXXFlKEtrSzNlXXFmKEtsSzhlXXFnKEttS2xlXXFoKEtuS2xlXXFpKEtvSzxlXXFqKEtwS29lXXFrKEtxS0BlXXFsKEtyS3FlXXFtKEtzS3JlXXFuKEtzSz9lXXFvKEt0S0RlXXFwKEt1S3RlXXFxKEt2SxBlXXFyKEt3SxNlXXFzKEt4SxRlXXF0KEt5SxhlXXF1KEt6SxtlXXF2KEt7SxxlXXF3KEt8Sx9lXXF4KEt9SyBlXXF5KEt+SyRlXXF6KEt/SydlXXF7KEuASyhlXXF8KEuBSytlXXF9KEuCSyxlXXF+KEuDSy9lXXF/KEuESzBlXXGAKEuFSzRlXXGBKEuGSzdlXXGCKEuHSzhlXXGDKEuISztlXXGEKEuJSzxlXXGFKEuKS0BlXXGGKEuLS0NlXXGHKEuMS0RlXXGIKEuNS0hlXXGJKEuOS0hlXXGKKEuPS0plXXGLKEuQS0tlXXGMKEuRS0xlXXGNKEuSS05lXXGOKEuTS1BlXXGPKEuUS1BlXXGQKEuVS1JlXXGRKEuWS1JlXXGSKEuXS1NlXXGTKEuYS1NlXXGUKEuZS1RlXXGVKEuaS1RlXXGWKEubS1VlXXGXKEucS1hlXXGYKEudS1hlXXGZKEueS1plXXGaKEufS1plXXGbKEugS1tlXXGcKEuhS1tlXXGdKEuiS1xlXXGeKEujS1xlXXGfKEukS11lXXGgKEulS11lXXGhKEumS19lXXGiKEunS19lXXGjKEuoS2FlXXGkKEupS2JlXXGlKEuqS2NlXXGmKEurS2ZlXXGnKEusS2dlXXGoKEutS2dlXXGpKEuuS2llXXGqKEuvS2llXXGrKEuwS2plXXGsKEuxS2plXXGtKEuyS2tlXXGuKEuzS2tlXXGvKEu0S2xlXXGwKEu1S29lXXGxKEu2S29lXXGyKEu3S3FlXXGzKEu4S3FlXXG0KEu5S3JlXXG1KEu6S3JlXXG2KEu7S3NlXXG3KEu8S3NlXXG4KEu9S3RlXXG5KEu+S3RlXXG6KEu/S3VlXXG7KEvAS1ZlXXG8KEvBS15lXXG9KEvCS1FlXXG+KEvDS1dlXXG/KEvES1dlXXHAKEvFS1dlXXHBKEvGS2hlXXHCKEvHS2VlXXHDKEvIS09lXXHEKEvJSw9lXXHFKEvKSw9lXXHGKEvLSw9lXXHHKEvMS21lXXHIKEvNS3BlXXHJKEvOS1llXXHKKEvPS25lXXHLKEvQS25lXXHMKEvRS25lXXHNKEvSS85lXXHOKEvTS85lXXHPKEvUS85lXXHQKEvVS81lXXHRKEvWS81lXXHSKEvXS81lZVUFbGFiZWxx00vOWAAAAAB9h1UIaGFsZmJvbmRx1EvOiH2HVQZyYWRpdXNx1UvORz/JmZmgAAAAfYdVC2xhYmVsT2Zmc2V0cdZLzk59h1UIZHJhd01vZGVx10vOSwB9h1UIb3B0aW9uYWxx2H1VB2Rpc3BsYXlx2UvOSwJ9h3Uu'))
	crdInfo = cPickle.loads(base64.b64decode('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'))
	surfInfo = {'category': (0, None, {}), 'probeRadius': (0, None, {}), 'pointSize': (0, None, {}), 'name': [], 'density': (0, None, {}), 'colorMode': (0, None, {}), 'useLighting': (0, None, {}), 'transparencyBlendMode': (0, None, {}), 'molecule': [], 'smoothLines': (0, None, {}), 'lineWidth': (0, None, {}), 'allComponents': (0, None, {}), 'twoSidedLighting': (0, None, {}), 'customVisibility': [], 'drawMode': (0, None, {}), 'display': (0, None, {}), 'customColors': []}
	vrmlInfo = {'subid': (0, None, {}), 'display': (0, None, {}), 'id': (0, None, {}), 'vrmlString': [], 'name': (0, None, {})}
	colors = {'Ru': ((0.141176, 0.560784, 0.560784), 1, u'default'), 'firebrick': ((0.698039, 0.133333, 0.133333), 1, u''), 'Re': ((0.14902, 0.490196, 0.670588), 1, u'default'), 'Rf': ((0.8, 0, 0.34902), 1, u'default'), 'Ra': ((0, 0.490196, 0), 1, u'default'), 'Rb': ((0.439216, 0.180392, 0.690196), 1, u'default'), 'Rn': ((0.258824, 0.509804, 0.588235), 1, u'default'), 'Rh': ((0.0392157, 0.490196, 0.54902), 1, u'default'), 'Be': ((0.760784, 1, 0), 1, u'default'), 'Ba': ((0, 0.788235, 0), 1, u'default'), 'Bh': ((0.878431, 0, 0.219608), 1, u'default'), 'Bi': ((0.619608, 0.309804, 0.709804), 1, u'default'), 'Bk': ((0.541176, 0.309804, 0.890196), 1, u'default'), 'Br': ((0.65098, 0.160784, 0.160784), 1, u'default'), 'H': ((1, 1, 1), 1, u'default'), 'Dy': ((0.121569, 1, 0.780392), 1, u'default'), 'P': ((1, 0.501961, 0), 1, u'default'), 'Os': ((0.14902, 0.4, 0.588235), 1, u'default'), 'Ge': ((0.4, 0.560784, 0.560784), 1, u'default'), 'Gd': ((0.270588, 1, 0.780392), 1, u'default'), 'Ga': ((0.760784, 0.560784, 0.560784), 1, u'default'), 'Pr': ((0.85098, 1, 0.780392), 1, u'default'),
'Pt': ((0.815686, 0.815686, 0.878431), 1, u'default'), 'Pu': ((0, 0.419608, 1), 1, u'default'), 'C': ((0.564706, 0.564706, 0.564706), 1, u'default'), 'Pb': ((0.341176, 0.34902, 0.380392), 1, u'default'), 'Pa': ((0, 0.631373, 1), 1, u'default'), 'Pd': ((0, 0.411765, 0.521569), 1, u'default'), 'Cd': ((1, 0.85098, 0.560784), 1, u'default'), 'Po': ((0.670588, 0.360784, 0), 1, u'default'), 'Pm': ((0.639216, 1, 0.780392), 1, u'default'), 'Hs': ((0.901961, 0, 0.180392), 1, u'default'), 'Ho': ((0, 1, 0.611765), 1, u'default'), 'Hf': ((0.301961, 0.760784, 1), 1, u'default'), 'Hg': ((0.721569, 0.721569, 0.815686), 1, u'default'), 'He': ((0.85098, 1, 1), 1, u'default'), 'Md': ((0.701961, 0.0509804, 0.65098), 1, u'default'), 'Mg': ((0.541176, 1, 0), 1, u'default'), 'K': ((0.560784, 0.25098, 0.831373), 1, u'default'), 'Mn': ((0.611765, 0.478431, 0.780392), 1, u'default'), 'O': ((1, 0.0509804, 0.0509804), 1, u'default'), 'Mt': ((0.921569, 0, 0.14902), 1, u'default'), 'S': ((1, 1, 0.188235), 1, u'default'), 'W': ((0.129412, 0.580392, 0.839216), 1, u'default'), 'Zn': ((0.490196, 0.501961, 0.690196), 1, u'default'),
'Eu': ((0.380392, 1, 0.780392), 1, u'default'), 'Zr': ((0.580392, 0.878431, 0.878431), 1, u'default'), 'Er': ((0, 0.901961, 0.458824), 1, u'default'), 'Ni': ((0.313725, 0.815686, 0.313725), 1, u'default'), 'No': ((0.741176, 0.0509804, 0.529412), 1, u'default'), 'Na': ((0.670588, 0.360784, 0.94902), 1, u'default'), 'Nb': ((0.45098, 0.760784, 0.788235), 1, u'default'), 'Nd': ((0.780392, 1, 0.780392), 1, u'default'), 'Ne': ((0.701961, 0.890196, 0.960784), 1, u'default'), 'Np': ((0, 0.501961, 1), 1, u'default'), 'Fr': ((0.258824, 0, 0.4), 1, u'default'), 'Fe': ((0.878431, 0.4, 0.2), 1, u'default'), 'Fm': ((0.701961, 0.121569, 0.729412), 1, u'default'), 'B': ((1, 0.709804, 0.709804), 1, u'default'), 'F': ((0.564706, 0.878431, 0.313725), 1, u'default'), 'Sr': ((0, 1, 0), 1, u'default'), 'N': ((0.188235, 0.313725, 0.972549), 1, u'default'), 'Kr': ((0.360784, 0.721569, 0.819608), 1, u'default'), 'Si': ((0.941176, 0.784314, 0.627451), 1, u'default'), 'Sn': ((0.4, 0.501961, 0.501961), 1, u'default'), 'Sm': ((0.560784, 1, 0.780392), 1, u'default'), 'V': ((0.65098, 0.65098, 0.670588), 1, u'default'),
'Sc': ((0.901961, 0.901961, 0.901961), 1, u'default'), 'Sb': ((0.619608, 0.388235, 0.709804), 1, u'default'), 'Sg': ((0.85098, 0, 0.270588), 1, u'default'), 'Se': ((1, 0.631373, 0), 1, u'default'), 'Co': ((0.941176, 0.564706, 0.627451), 1, u'default'), 'Cm': ((0.470588, 0.360784, 0.890196), 1, u'default'), 'Cl': ((0.121569, 0.941176, 0.121569), 1, u'default'), 'Ca': ((0.239216, 1, 0), 1, u'default'), 'Cf': ((0.631373, 0.211765, 0.831373), 1, u'default'), 'Ce': ((1, 1, 0.780392), 1, u'default'), 'Xe': ((0.258824, 0.619608, 0.690196), 1, u'default'), 'Tm': ((0, 0.831373, 0.321569), 1, u'default'), 'Cs': ((0.341176, 0.0901961, 0.560784), 1, u'default'), 'Cr': ((0.541176, 0.6, 0.780392), 1, u'default'), 'Cu': ((0.784314, 0.501961, 0.2), 1, u'default'), 'La': ((0.439216, 0.831373, 1), 1, u'default'), 'Li': ((0.8, 0.501961, 1), 1, u'default'), 'Tl': ((0.65098, 0.329412, 0.301961), 1, u'default'), 'Lu': ((0, 0.670588, 0.141176), 1, u'default'), 'Lr': ((0.780392, 0, 0.4), 1, u'default'), 'Th': ((0, 0.729412, 1), 1, u'default'), 'Ti': ((0.74902, 0.760784, 0.780392), 1, u'default'),
'tan': ((0.823529, 0.705882, 0.54902), 1, u'default'), 'Te': ((0.831373, 0.478431, 0), 1, u'default'), 'Tb': ((0.188235, 1, 0.780392), 1, u'default'), 'Tc': ((0.231373, 0.619608, 0.619608), 1, u'default'), 'Ta': ((0.301961, 0.65098, 1), 1, u'default'), 'Yb': ((0, 0.74902, 0.219608), 1, u'default'), 'Db': ((0.819608, 0, 0.309804), 1, u'default'), 'navy blue': ((0, 0, 0.501961), 1, u''), 'At': ((0.458824, 0.309804, 0.270588), 1, u'default'), 'I': ((0.580392, 0, 0.580392), 1, u'default'), 'U': ((0, 0.560784, 1), 1, u'default'), 'Y': ((0.580392, 1, 1), 1, u'default'), 'Ac': ((0.439216, 0.670588, 0.980392), 1, u'default'), 'Ag': ((0.752941, 0.752941, 0.752941), 1, u'default'), 'Ir': ((0.0901961, 0.329412, 0.529412), 1, u'default'), 'Am': ((0.329412, 0.360784, 0.94902), 1, u'default'), 'Al': ((0.74902, 0.65098, 0.65098), 1, u'default'), 'As': ((0.741176, 0.501961, 0.890196), 1, u'default'), 'Ar': ((0.501961, 0.819608, 0.890196), 1, u'default'), 'Au': ((1, 0.819608, 0.137255), 1, u'default'), 'Es': ((0.701961, 0.121569, 0.831373), 1, u'default'), 'In': ((0.65098, 0.458824, 0.45098), 1, u'default'),
'Mo': ((0.329412, 0.709804, 0.709804), 1, u'default')}
	materials = {u'default': ((1, 1, 1), 30), u'': ((1, 1, 1), 30)}
	pbInfo = {'category': [u'distance monitor'], 'bondInfo': [{'color': (0, None, {}), 'atoms': [], 'label': (0, None, {}), 'halfbond': (0, None, {}), 'labelColor': (0, None, {}), 'drawMode': (0, None, {}), 'display': (0, None, {})}], 'lineType': (1, 2, {}), 'color': (1, 20, {}), 'optional': {'fixedLabels': (True, False, (1, False, {}))}, 'display': (1, True, {}), 'showStubBonds': (1, False, {}), 'lineWidth': (1, 1, {}), 'stickScale': (1, 1, {}), 'id': [-2]}
	modelAssociations = {}
	colorInfo = (23, (u'', (0, 0.923077, 1, 1)), {(u'', (1, 0.307692, 0, 1)): [13], (u'tan', (0.823529, 0.705882, 0.54902, 1)): [0], (u'', (1, 0.923077, 0, 1)): [11], (u'red', (1, 0, 0, 1)): [14], (u'', (0, 1, 0.461538, 1)): [6], (u'H', (1, 1, 1, 1)): [17], (u'', (1, 0.615385, 0, 1)): [12], (u'N', (0.188235, 0.313725, 0.972549, 1)): [15], (u'P', (1, 0.501961, 0, 1)): [18], (u'black', (0, 0, 0, 1)): [21], (u'', (0.769231, 1, 0, 1)): [10], (u'', (0, 0.307692, 1, 1)): [2], (u'O', (1, 0.0509804, 0.0509804, 1)): [16], (u'', (0, 1, 0.153846, 1)): [7], (u'yellow', (1, 1, 0, 1)): [20], (u'', (0, 0.615385, 1, 1)): [3], (u'', (0.153846, 1, 0, 1)): [8], (u'C', (0.564706, 0.564706, 0.564706, 1)): [19], (u'', (0.461538, 1, 0, 1)): [9], (u'green', (0, 1, 0, 1)): [22], (u'', (0, 1, 0.769231, 1)): [5], (u'blue', (0, 0, 1, 1)): [1]})
	viewerInfo = {'cameraAttrs': {'center': (-1.3236819133468, -2.0857618540728, 2.3881045085536), 'fieldOfView': 20.425371539944, 'nearFar': (23.812751407706, -21.822977284201), 'ortho': False, 'eyeSeparation': 50.8, 'focal': 4.9005750977789}, 'viewerAttrs': {'silhouetteColor': None, 'clipping': False, 'showSilhouette': False, 'showShadows': False, 'viewSize': 15.90032464339, 'labelsOnTop': True, 'depthCueRange': (0.5, 1), 'silhouetteWidth': 2, 'singleLayerTransparency': True, 'shadowTextureSize': 2048, 'backgroundImage': [None, 1, 2, 1, 0, 0], 'backgroundGradient': [('Chimera default', [(1, 1, 1, 1), (0, 0, 1, 1)], 1), 1, 0, 0], 'depthCue': True, 'highlight': 0, 'scaleFactor': 1.176712787438, 'angleDependentTransparency': True, 'backgroundMethod': 0}, 'viewerHL': 22, 'cameraMode': 'mono', 'detail': 1.5, 'viewerFog': None, 'viewerBG': 21}

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
	formattedPositions = {'session-start': (1.0, 15.447685517708, (-1.3236819133468, -2.0857618540728, 4.9005750977789), (23.033140857194, -16.969308710237), 4.9005750977789, {(0, 0): ((0.0, 0.0, 0.0), (0.0, 0.0, 1.0, 0.0))}, {(0, 0, 'Molecule'): (False, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, False, 5.0)}, 4, (-2.465584545844525, 0.13607471441173136, 3.0319160734783974), False, 20.425371539944)}
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

	curSelIds =  [215]
	savedSels = []
	openModelsAttrs = { 'cofrMethod': 4 }
	windowSize = (1920, 1106)
	xformMap = {0: (((0.31805794476161, 0.6314454776304, 0.70718862586592), 88.099469437601), (-2.3839946858406, -10.01256057288, 0.79261356765516), True)}
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

