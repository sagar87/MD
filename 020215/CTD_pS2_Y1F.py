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
	resInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVQZpbnNlcnRxAksOVQEgfYdVC2ZpbGxEaXNwbGF5cQNLDol9h1UEbmFtZXEESw5YAwAAAFNFUn1xBShYAwAAAFBST11xBihLAksFSwlLDGVYAwAAAFVOS11xB0sBYVgDAAAAVkFMXXEIKEsDSwplWAMAAABQSEVdcQkoSwBLB2V1h1UFY2hhaW5xCksOWAEAAABBfYdVDnJpYmJvbkRyYXdNb2RlcQtLDksCfYdVAnNzcQxLDomJhn2HVQhtb2xlY3VsZXENSw5LAH2HVQtyaWJib25Db2xvcnEOSw5LAX1xDyhLAk5dcRBLAUsBhnERYYZLA05dcRJLAksBhnETYYZLBE5dcRRLA0sBhnEVYYZLBU5dcRZLBEsBhnEXYYZLBk5dcRhLBUsBhnEZYYZLB05dcRpLBksBhnEbYYZLCE5dcRxLB0sBhnEdYYZLCU5dcR5LCEsBhnEfYYZLCk5dcSBLCUsBhnEhYYZLC05dcSJLCksBhnEjYYZLDE5dcSRLC0sBhnElYYZLDU5dcSZLDEsBhnEnYYZLDk5dcShLDUsBhnEpYYZ1h1UFbGFiZWxxKksOWAAAAAB9h1UKbGFiZWxDb2xvcnErSw5OfYdVCGZpbGxNb2RlcSxLDksBfYdVBWlzSGV0cS1LDol9h1ULbGFiZWxPZmZzZXRxLksOTn2HVQhwb3NpdGlvbnEvXXEwSwFLDoZxMWFVDXJpYmJvbkRpc3BsYXlxMksOiX2HVQhvcHRpb25hbHEzfVUEc3NJZHE0Sw5K/////32HdS4='))
	atomInfo = cPickle.loads(base64.b64decode('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'))
	bondInfo = cPickle.loads(base64.b64decode('gAJ9cQEoVQVjb2xvcnECS9BOfYdVBWF0b21zcQNdcQQoXXEFKEsQSw9lXXEGKEsRSxBlXXEHKEsSSxFlXXEIKEsTSxFlXXEJKEsUSxNlXXEKKEsVSxRlXXELKEsWSxVlXXEMKEsXSxVlXXENKEsYSxdlXXEOKEsZSxhlXXEPKEsaSxllXXEQKEsbSxllXXERKEscSxtlXXESKEsdSxxlXXETKEseSx1lXXEUKEsfSx1lXXEVKEsgSx9lXXEWKEshSyBlXXEXKEsiSyFlXXEYKEsjSyFlXXEZKEskSyNlXXEaKEslSyRlXXEbKEsmSyVlXXEcKEsnSyVlXXEdKEsoSydlXXEeKEspSyhlXXEfKEsqSyllXXEgKEsrSyllXXEhKEssSytlXXEiKEstSyxlXXEjKEsuSy1lXXEkKEsvSy1lXXElKEswSy9lXXEmKEsxSzBlXXEnKEsySzFlXXEoKEszSzFlXXEpKEs0SzNlXXEqKEs1SzRlXXErKEs2SzVlXXEsKEs3SzVlXXEtKEs4SzdlXXEuKEs5SzhlXXEvKEs6SzllXXEwKEs7SzllXXExKEs8SztlXXEyKEs9SzxlXXEzKEs+Sz1lXXE0KEs/Sz1lXXE1KEtASz9lXXE2KEtBS0BlXXE3KEtCS0FlXXE4KEtDS0FlXXE5KEtES0NlXXE6KEtFS0RlXXE7KEtGS0VlXXE8KEtHS0VlXXE9KEtISxBlXXE+KEtJS0hlXXE/KEtKS0llXXFAKEtLS0llXXFBKEtMS0tlXXFCKEtNS0xlXXFDKEtOS01lXXFEKEtOS0plXXFFKEtPSxRlXXFGKEtQS09lXXFHKEtRSxhlXXFIKEtSS1FlXXFJKEtTS1JlXXFKKEtTSxdlXXFLKEtUSxxlXXFMKEtVS1RlXXFNKEtWS1RlXXFOKEtXSyBlXXFPKEtYS1dlXXFQKEtZSyRlXXFRKEtaS1llXXFSKEtbS1plXXFTKEtbSyNlXXFUKEtcSyhlXXFVKEtdS1xlXXFWKEteSyxlXXFXKEtfS15lXXFYKEtgS19lXXFZKEthS19lXXFaKEtiS2FlXXFbKEtjS2JlXXFcKEtkS2NlXXFdKEtkS2BlXXFeKEtlSzBlXXFfKEtmS2VlXXFgKEtnSzRlXXFhKEtoS2dlXXFiKEtpS2hlXXFjKEtpSzNlXXFkKEtqSzhlXXFlKEtrS2plXXFmKEtsS2plXXFnKEttSzxlXXFoKEtuS21lXXFpKEtvS0BlXXFqKEtwS29lXXFrKEtxS3BlXXFsKEtxSz9lXXFtKEtyS0RlXXFuKEtzS3JlXXFvKEt0SxBlXXFwKEt1SxNlXXFxKEt2SxRlXXFyKEt3SxhlXXFzKEt4SxtlXXF0KEt5SxxlXXF1KEt6Sx9lXXF2KEt7SyBlXXF3KEt8SyRlXXF4KEt9SydlXXF5KEt+SyhlXXF6KEt/SytlXXF7KEuASyxlXXF8KEuBSy9lXXF9KEuCSzBlXXF+KEuDSzRlXXF/KEuESzdlXXGAKEuFSzhlXXGBKEuGSztlXXGCKEuHSzxlXXGDKEuIS0BlXXGEKEuJS0NlXXGFKEuKS0RlXXGGKEuLS0hlXXGHKEuMS0hlXXGIKEuNS0plXXGJKEuOS0tlXXGKKEuPS0xlXXGLKEuQS01lXXGMKEuRS05lXXGNKEuSS09lXXGOKEuTS09lXXGPKEuUS1FlXXGQKEuVS1FlXXGRKEuWS1JlXXGSKEuXS1JlXXGTKEuYS1NlXXGUKEuZS1NlXXGVKEuaS1RlXXGWKEubS1dlXXGXKEucS1dlXXGYKEudS1llXXGZKEueS1llXXGaKEufS1plXXGbKEugS1plXXGcKEuhS1tlXXGdKEuiS1tlXXGeKEujS1xlXXGfKEukS1xlXXGgKEulS15lXXGhKEumS15lXXGiKEunS2BlXXGjKEuoS2FlXXGkKEupS2JlXXGlKEuqS2NlXXGmKEurS2RlXXGnKEusS2VlXXGoKEutS2VlXXGpKEuuS2dlXXGqKEuvS2dlXXGrKEuwS2hlXXGsKEuxS2hlXXGtKEuyS2llXXGuKEuzS2llXXGvKEu0S2plXXGwKEu1S21lXXGxKEu2S21lXXGyKEu3S29lXXGzKEu4S29lXXG0KEu5S3BlXXG1KEu6S3BlXXG2KEu7S3FlXXG3KEu8S3FlXXG4KEu9S3JlXXG5KEu+S3JlXXG6KEu/S2xlXXG7KEvAS2xlXXG8KEvBS2xlXXG9KEvCS11lXXG+KEvDS2ZlXXG/KEvES3NlXXHAKEvFS1VlXXHBKEvGS1VlXXHCKEvHS1VlXXHDKEvISw9lXXHEKEvJSw9lXXHFKEvKSw9lXXHGKEvLS1hlXXHHKEvMS1ZlXXHIKEvNS1ZlXXHJKEvOS1ZlXXHKKEvPS1BlXXHLKEvQS2tlXXHMKEvRS2tlXXHNKEvSS2tlXXHOKEvTS25lXXHPKEvUS89lXXHQKEvVS89lXXHRKEvWS89lXXHSKEvXS8NlXXHTKEvYS8NlXXHUKEvZS8NlZVUFbGFiZWxx1UvQWAAAAAB9h1UIaGFsZmJvbmRx1kvQiH2HVQZyYWRpdXNx10vQRz/JmZmgAAAAfYdVC2xhYmVsT2Zmc2V0cdhL0E59h1UIZHJhd01vZGVx2UvQSwF9h1UIb3B0aW9uYWxx2n1VB2Rpc3BsYXlx20vQSwJ9h3Uu'))
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
	colorInfo = (23, (u'', (0, 0.923077, 1, 1)), {(u'', (1, 0.307692, 0, 1)): [13], (u'tan', (0.823529, 0.705882, 0.54902, 1)): [0], (u'', (1, 0.923077, 0, 1)): [11], (u'red', (1, 0, 0, 1)): [14], (u'', (0, 1, 0.461538, 1)): [6], (u'H', (1, 1, 1, 1)): [17], (u'', (1, 0.615385, 0, 1)): [12], (u'N', (0.188235, 0.313725, 0.972549, 1)): [15], (u'P', (1, 0.501961, 0, 1)): [18], (u'', (0.769231, 1, 0, 1)): [10], (u'', (0, 0.307692, 1, 1)): [2], (u'O', (1, 0.0509804, 0.0509804, 1)): [16], (u'', (0, 1, 0.153846, 1)): [7], (u'yellow', (1, 1, 0, 1)): [20], (u'', (0, 0.615385, 1, 1)): [3], (u'', (0.153846, 1, 0, 1)): [8], (u'C', (0.564706, 0.564706, 0.564706, 1)): [19], (u'', (0.461538, 1, 0, 1)): [9], (u'green', (0, 1, 0, 1)): [22], (u'white', (1, 1, 1, 1)): [21], (u'', (0, 1, 0.769231, 1)): [5], (u'blue', (0, 0, 1, 1)): [1]})
	viewerInfo = {'cameraAttrs': {'center': (-1.6445754123434, -1.6874403207658, -5.811612738952), 'fieldOfView': 40.246463653063, 'nearFar': (7.0389761494084, -38.822170040977), 'ortho': False, 'eyeSeparation': 50.8, 'focal': 2.8086079087528}, 'viewerAttrs': {'silhouetteColor': None, 'clipping': False, 'showSilhouette': False, 'showShadows': False, 'viewSize': 21.421592435998, 'labelsOnTop': True, 'depthCueRange': (0.5, 1), 'silhouetteWidth': 2, 'singleLayerTransparency': True, 'shadowTextureSize': 2048, 'backgroundImage': [None, 1, 2, 1, 0, 0], 'backgroundGradient': [('Chimera default', [(1, 1, 1, 1), (0, 0, 1, 1)], 1), 1, 0, 0], 'depthCue': True, 'highlight': 0, 'scaleFactor': 0.91025313326598, 'angleDependentTransparency': True, 'backgroundMethod': 0}, 'viewerHL': 22, 'cameraMode': 'mono', 'detail': 5, 'viewerFog': None, 'viewerBG': 21}

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
	userScalings = [('licorice', [[0.35, 0.35], [0.35, 0.35], [0.35, 0.35], [0.35, 0.35, 0.35, 0.35], [0.35, 0.35]])]
	userXSections = []
	userResidueClasses = []
	residueData = [(1, 'licorice', 'rounded', u'amino acid'), (2, 'licorice', 'rounded', u'amino acid'), (3, 'licorice', 'rounded', u'amino acid'), (4, 'licorice', 'rounded', u'amino acid'), (5, 'licorice', 'rounded', u'amino acid'), (6, 'licorice', 'rounded', u'amino acid'), (7, 'licorice', 'rounded', u'amino acid'), (8, 'licorice', 'rounded', u'amino acid'), (9, 'licorice', 'rounded', u'amino acid'), (10, 'licorice', 'rounded', u'amino acid'), (11, 'licorice', 'rounded', u'amino acid'), (12, 'licorice', 'rounded', u'amino acid'), (13, 'licorice', 'rounded', u'amino acid'), (14, 'licorice', 'rounded', u'amino acid')]
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
	openModelsAttrs = { 'cofrMethod': 0 }
	from chimera import Point
	openModelsAttrs['cofr'] = Point(-12.3027, -4.10455, -5.81161)
	windowSize = (1920, 1106)
	xformMap = {0: (((0.81549003071098, -0.39260398915677, -0.42525065256763), 156.86374544953), (-15.305770843997, -11.253724863867, -14.281719437829), True)}
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

