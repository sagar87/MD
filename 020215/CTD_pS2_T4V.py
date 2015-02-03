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
	resInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVQZpbnNlcnRxAksOVQEgfYdVC2ZpbGxEaXNwbGF5cQNLDol9h1UEbmFtZXEESw5YAwAAAFNFUn1xBShYAwAAAFBST11xBihLAksFSwlLDGVYAwAAAFZBTF1xByhLA0sKZVgDAAAAVFlSXXEIKEsASwdldYdVBWNoYWlucQlLDlgBAAAAQX2HVQ5yaWJib25EcmF3TW9kZXEKSw5LAn2HVQJzc3ELSw6JiYZ9h1UIbW9sZWN1bGVxDEsOSwB9h1ULcmliYm9uQ29sb3JxDUsOTn2HVQVsYWJlbHEOSw5YAAAAAH2HVQpsYWJlbENvbG9ycQ9LDk59h1UIZmlsbE1vZGVxEEsOSwF9h1UFaXNIZXRxEUsOiX2HVQtsYWJlbE9mZnNldHESSw5OfYdVCHBvc2l0aW9ucRNdcRRLAUsOhnEVYVUNcmliYm9uRGlzcGxheXEWSw6JfYdVCG9wdGlvbmFscRd9VQRzc0lkcRhLDkr/////fYd1Lg=='))
	atomInfo = cPickle.loads(base64.b64decode('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'))
	bondInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVQVjb2xvcnECS9JOfYdVBWF0b21zcQNdcQQoXXEFKEsQSw9lXXEGKEsRSxBlXXEHKEsSSxFlXXEIKEsTSxFlXXEJKEsUSxNlXXEKKEsVSxRlXXELKEsWSxVlXXEMKEsXSxVlXXENKEsYSxdlXXEOKEsZSxhlXXEPKEsaSxllXXEQKEsbSxllXXERKEscSxtlXXESKEsdSxxlXXETKEseSx1lXXEUKEsfSx1lXXEVKEsgSx9lXXEWKEshSyBlXXEXKEsiSyFlXXEYKEsjSyFlXXEZKEskSyNlXXEaKEslSyRlXXEbKEsmSyVlXXEcKEsnSyVlXXEdKEsoSydlXXEeKEspSyhlXXEfKEsqSyllXXEgKEsrSyllXXEhKEssSytlXXEiKEstSyxlXXEjKEsuSy1lXXEkKEsvSy1lXXElKEswSy9lXXEmKEsxSzBlXXEnKEsySzFlXXEoKEszSzFlXXEpKEs0SzNlXXEqKEs1SzRlXXErKEs2SzVlXXEsKEs3SzVlXXEtKEs4SzdlXXEuKEs5SzhlXXEvKEs6SzllXXEwKEs7SzllXXExKEs8SztlXXEyKEs9SzxlXXEzKEs+Sz1lXXE0KEs/Sz1lXXE1KEtASz9lXXE2KEtBS0BlXXE3KEtCS0FlXXE4KEtDS0FlXXE5KEtES0NlXXE6KEtFS0RlXXE7KEtGS0VlXXE8KEtHS0VlXXE9KEtISxBlXXE+KEtJS0hlXXE/KEtKS0llXXFAKEtLS0llXXFBKEtMS0tlXXFCKEtNS0xlXXFDKEtOS01lXXFEKEtPS01lXXFFKEtPS0plXXFGKEtQSxRlXXFHKEtRS1BlXXFIKEtSSxhlXXFJKEtTS1JlXXFKKEtUS1NlXXFLKEtUSxdlXXFMKEtVSxxlXXFNKEtWS1VlXXFOKEtXS1VlXXFPKEtYSyBlXXFQKEtZS1hlXXFRKEtaSyRlXXFSKEtbS1plXXFTKEtcS1tlXXFUKEtcSyNlXXFVKEtdSyhlXXFWKEteS11lXXFXKEtfSyxlXXFYKEtgS19lXXFZKEthS2BlXXFaKEtiS2BlXXFbKEtjS2JlXXFcKEtkS2NlXXFdKEtlS2RlXXFeKEtmS2RlXXFfKEtlS2FlXXFgKEtnSzBlXXFhKEtoS2dlXXFiKEtpSzRlXXFjKEtqS2llXXFkKEtrS2plXXFlKEtrSzNlXXFmKEtsSzhlXXFnKEttS2xlXXFoKEtuS2xlXXFpKEtvSzxlXXFqKEtwS29lXXFrKEtxS0BlXXFsKEtyS3FlXXFtKEtzS3JlXXFuKEtzSz9lXXFvKEt0S0RlXXFwKEt1S3RlXXFxKEt2SxBlXXFyKEt3SxNlXXFzKEt4SxRlXXF0KEt5SxhlXXF1KEt6SxtlXXF2KEt7SxxlXXF3KEt8Sx9lXXF4KEt9SyBlXXF5KEt+SyRlXXF6KEt/SydlXXF7KEuASyhlXXF8KEuBSytlXXF9KEuCSyxlXXF+KEuDSy9lXXF/KEuESzBlXXGAKEuFSzRlXXGBKEuGSzdlXXGCKEuHSzhlXXGDKEuISztlXXGEKEuJSzxlXXGFKEuKS0BlXXGGKEuLS0NlXXGHKEuMS0RlXXGIKEuNS0hlXXGJKEuOS0hlXXGKKEuPS0plXXGLKEuQS0tlXXGMKEuRS0xlXXGNKEuSS09lXXGOKEuTS1BlXXGPKEuUS1BlXXGQKEuVS1JlXXGRKEuWS1JlXXGSKEuXS1NlXXGTKEuYS1NlXXGUKEuZS1RlXXGVKEuaS1RlXXGWKEubS1VlXXGXKEucS1hlXXGYKEudS1hlXXGZKEueS1plXXGaKEufS1plXXGbKEugS1tlXXGcKEuhS1tlXXGdKEuiS1xlXXGeKEujS1xlXXGfKEukS11lXXGgKEulS11lXXGhKEumS19lXXGiKEunS19lXXGjKEuoS2FlXXGkKEupS2JlXXGlKEuqS2NlXXGmKEurS2VlXXGnKEusS2dlXXGoKEutS2dlXXGpKEuuS2llXXGqKEuvS2llXXGrKEuwS2plXXGsKEuxS2plXXGtKEuyS2tlXXGuKEuzS2tlXXGvKEu0S2xlXXGwKEu1S29lXXGxKEu2S29lXXGyKEu3S3FlXXGzKEu4S3FlXXG0KEu5S3JlXXG1KEu6S3JlXXG2KEu7S3NlXXG3KEu8S3NlXXG4KEu9S3RlXXG5KEu+S3RlXXG6KEu/S3VlXXG7KEvAS15lXXG8KEvBS2ZlXXG9KEvCS2hlXXG+KEvDS1llXXG/KEvES1dlXXHAKEvFS1dlXXHBKEvGS1dlXXHCKEvHS1FlXXHDKEvIS25lXXHEKEvJS25lXXHFKEvKS25lXXHGKEvLS1ZlXXHHKEvMS1ZlXXHIKEvNS1ZlXXHJKEvOSw9lXXHKKEvPSw9lXXHLKEvQSw9lXXHMKEvRS3BlXXHNKEvSS05lXXHOKEvTS21lXXHPKEvUS21lXXHQKEvVS21lXXHRKEvWS8dlXXHSKEvXS8dlXXHTKEvYS8dlXXHUKEvZS8JlXXHVKEvaS8JlXXHWKEvbS8JlZVUFbGFiZWxx10vSWAAAAAB9h1UIaGFsZmJvbmRx2EvSiH2HVQZyYWRpdXNx2UvSRz/JmZmgAAAAfYdVC2xhYmVsT2Zmc2V0cdpL0k59h1UIZHJhd01vZGVx20vSSwB9h1UIb3B0aW9uYWxx3H1VB2Rpc3BsYXlx3UvSSwJ9h3Uu'))
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
	pbInfo = {'category': [u'distance monitor'], 'bondInfo': [{'color': (0, None, {}), 'atoms': [], 'label': (0, None, {}), 'halfbond': (0, None, {}), 'labelColor': (0, None, {}), 'drawMode': (0, None, {}), 'display': (0, None, {})}], 'lineType': (1, 2, {}), 'color': (1, 6, {}), 'optional': {'fixedLabels': (True, False, (1, False, {}))}, 'display': (1, True, {}), 'showStubBonds': (1, False, {}), 'lineWidth': (1, 1, {}), 'stickScale': (1, 1, {}), 'id': [-2]}
	modelAssociations = {}
	colorInfo = (9, (u'H', (1, 1, 1, 1)), {(u'green', (0, 1, 0, 1)): [8], (u'N', (0.188235, 0.313725, 0.972549, 1)): [1], (u'P', (1, 0.501961, 0, 1)): [4], (u'O', (1, 0.0509804, 0.0509804, 1)): [2], (u'black', (0, 0, 0, 1)): [7], (u'tan', (0.823529, 0.705882, 0.54902, 1)): [0], (u'yellow', (1, 1, 0, 1)): [6], (u'C', (0.564706, 0.564706, 0.564706, 1)): [5]})
	viewerInfo = {'cameraAttrs': {'center': (-1.3236782593836, -2.0847760974122, 1.5638007977082), 'fieldOfView': 40.246463653063, 'nearFar': (38.418336281626, -7.3422894634887), 'ortho': False, 'eyeSeparation': 50.8, 'focal': 2.3998743827034}, 'viewerAttrs': {'silhouetteColor': None, 'clipping': False, 'showSilhouette': False, 'showShadows': False, 'viewSize': 18.620056544985, 'labelsOnTop': True, 'depthCueRange': (0.5, 1), 'silhouetteWidth': 2, 'singleLayerTransparency': True, 'shadowTextureSize': 2048, 'backgroundImage': [None, 1, 2, 1, 0, 0], 'backgroundGradient': [('Chimera default', [(1, 1, 1, 1), (0, 0, 1, 1)], 1), 1, 0, 0], 'depthCue': True, 'highlight': 0, 'scaleFactor': 0.44119690152339, 'angleDependentTransparency': True, 'backgroundMethod': 0}, 'viewerHL': 8, 'cameraMode': 'mono', 'detail': 1.5, 'viewerFog': None, 'viewerBG': 7}

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
	formattedPositions = {}
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

trPickle = 'gAJjQW5pbWF0ZS5UcmFuc2l0aW9ucwpUcmFuc2l0aW9ucwpxASmBcQJ9cQMoVQxjdXN0b21fc2NlbmVxBGNBbmltYXRlLlRyYW5zaXRpb24KVHJhbnNpdGlvbgpxBSmBcQZ9cQcoVQZmcmFtZXNxCEsBVQ1kaXNjcmV0ZUZyYW1lcQlLAVUKcHJvcGVydGllc3EKXXELVQNhbGxxDGFVBG5hbWVxDWgEVQRtb2RlcQ5VBmxpbmVhcnEPdWJVCGtleWZyYW1lcRBoBSmBcRF9cRIoaAhLFGgJSwFoCl1xE2gMYWgNaBBoDmgPdWJVBXNjZW5lcRRoBSmBcRV9cRYoaAhLAWgJSwFoCl1xF2gMYWgNaBRoDmgPdWJ1Yi4='
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
	Lighting._setFromParams({'ratio': 1.25, 'brightness': 1.16, 'material': [30.0, (1.0, 1.0, 1.0), 1], 'back': [(0.35740674433659325, 0.6604015517481454, -0.6604015517481455), (1.0, 1.0, 1.0), 0.0], 'mode': 'two-point', 'key': [(-0.35740674433659325, 0.6604015517481454, 0.6604015517481455), (1.0, 1.0, 1.0), 1.0], 'contrast': 0.83, 'fill': [(0.25056280708573153, 0.25056280708573153, 0.9351131265310293), (1.0, 1.0, 1.0), 0.0]})
try:
	restoreLightController()
except:
	reportRestoreError("Error restoring lighting parameters")

info = [(404, 194, 0, 1)]
try:
	from BondRotMgr import bondRotMgr
	bondRotMgr._sessionRestore(info, version=2)
except:
	reportRestoreError("Error restoring bond rotations")


try:
	from BuildStructure.gui import _sessionRestore
	_sessionRestore({'adjust torsions': {'decimal places': 3, 'labels': 'None', 'show degree symbol': 1}, 'mapped': 0})
except:
	reportRestoreError("Failure restoring Build Structure")


def restoreRemainder():
	from SimpleSession.versions.v62 import restoreWindowSize, \
	     restoreOpenStates, restoreSelections, restoreFontInfo, \
	     restoreOpenModelsAttrs, restoreModelClip, restoreSilhouettes

	curSelIds =  [217]
	savedSels = []
	openModelsAttrs = { 'cofrMethod': 0 }
	from chimera import Point
	openModelsAttrs['cofr'] = Point(-2.42626, -2.47625, 6.40407)
	windowSize = (1920, 1106)
	xformMap = {0: (((-0.35572882819766, 0.84501852019633, -0.39925017384382), 125.16526886225), (-4.5266497991296, -1.8765304457926, 14.000939602378), True)}
	fontInfo = {'face': ('Sans Serif', 'Normal', 16)}
	clipPlaneInfo = {}
	silhouettes = {0: True, 430: True}

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

