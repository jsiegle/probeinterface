from probeinterface import read_prb, write_prb
from probeinterface import generate_fake_probe, generate_fake_probe_bunch
from probeinterface import write_probeinterface, read_probeinterface

from pathlib import Path
import numpy as np

import pytest


folder = Path(__file__).absolute().parent



def test_probeinterface_format():
    filename = 'test_pi_format.h5'
    probebunch = generate_fake_probe_bunch()
    write_probeinterface(filename, probebunch)
    
    probebunch2 = read_probeinterface(filename)
    
    assert len(probebunch.probes) == len(probebunch.probes)
    
    for i in range(len(probebunch.probes)):
        probe0 = probebunch.probes[i]
        probe1 = probebunch2.probes[i]
        
        assert probe0.get_electrode_count() == probe1.get_electrode_count()
        assert np.allclose(probe0.electrode_positions,probe1.electrode_positions)
        assert np.allclose(probe0.probe_shape_vertices,probe1.probe_shape_vertices)
        
        # TODO more test

    #~ from probeinterface.plotting import plot_probe_bunch
    #~ import matplotlib.pyplot as plt
    #~ plot_probe_bunch(probebunch, with_channel_index=True, separate_axes=True)
    #~ plot_probe_bunch(probebunch2, with_channel_index=True, separate_axes=True)
    #~ plt.show()

    

prb_two_tetrodes = """
channel_groups = {
    0: {
            'channels' : [0,1,2,3],
            'geometry': {
                0: [0, 50],
                1: [50, 0],
                2: [0, -50],
                3: [-50, 0],
            }
    },
    1: {
            'channels' : [4,5,6,7],
            'geometry': {
                4: [0, 50],
                5: [50, 0],
                6: [0, -50],
                7: [-50, 0],
            }
    }
}
"""

def test_prb():
    probebunch = read_prb(folder / 'fake.prb')
    
    with open('two_tetrodes.prb', 'w') as f:
        f.write(prb_two_tetrodes)
    
    two_tetrode = read_prb('two_tetrodes.prb')
    assert len(two_tetrode.probes) == 2
    assert two_tetrode.probes[0].get_electrode_count() == 4
    
    write_prb('two_tetrodes.prb', two_tetrode)
    
    
    
    from probeinterface.plotting import plot_probe_bunch
    import matplotlib.pyplot as plt
    plot_probe_bunch(probebunch, with_channel_index=True, separate_axes=True)
    plt.show()
    
def test_generate():
    probe = generate_fake_probe()
    probebunch = generate_fake_probe_bunch()



if __name__ == '__main__':
    test_probeinterface_format()
    #~ test_prb()
    #~ test_generate()