Texto=""" título: Experiences in Developing a Distributed Agent-based Modeling Toolkit
with Python
resumen: Distributed agent-based modeling (ABM) on high-performance computing resources
provides the promise of capturing unprecedented details of large-scale complex systems.
However, the specialized knowledge required for developing such ABMs creates barriers to
wider adoption and utilization. Here we present our experiences in developing an initial
implementation of Repast4Py, a Python-based distributed ABM toolkit. We build on our
experiences in developing ABM toolkits, including Repast for High Performance Computing
(Repast HPC), to identify the key elements of a useful distributed ABM toolkit. We leverage
the Numba, NumPy, and PyTorch packages and the Python C-API to create a scalable modeling
system that can exploit the largest HPC resources and emerging computing architectures.
"""

def rank_orations(Texto, text_counter):
    orations = Texto.split('.')
    for oration in orations:
        len_oration = len(oration.split())
        match len_oration:
            case len_oration if len_oration <= 12:
                text_counter['Easy read'] += 1
            case  len_oration if len_oration <= 17:
                text_counter['Aceptable read'] += 1
            case  len_oration if len_oration <= 25:
                text_counter['Hard read'] += 1
            case  len_oration if len_oration > 25:
                text_counter['Very hard read'] += 1
