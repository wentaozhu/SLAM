import h5py 
import numpy as np

if __name__ == '__main__':
    h5f1 = h5py.File('FlowNet2.h5', 'w')

    h5f = h5py.File('./FlowNet2_weights.caffemodel.h5')
    # print(type(h5f), h5f.keys(), type(h5f['data']))
    for k in h5f['data'].keys():
        # print(k, h5f['data'][k].keys())
        if len(h5f['data'][k].keys()) != 0:
            # if len(h5f['data'][k].keys()) > 2:
            #     print(k, h5f['data'][k].keys())
            #     break
            for i, kk in enumerate(h5f['data'][k].keys()):
                if i == 0:
                    print(k+'_'+kk, h5f['data'][k][kk].shape, type(h5f['data'][k][kk]))
                    h5f1.create_dataset(k+'_'+kk, data=h5f['data'][k][kk])
                else:
                    print(k+'_'+kk, h5f['data'][k][kk].shape, type(h5f['data'][k][kk]))
                    h5f1.create_dataset(k+'_'+kk, data=h5f['data'][k][kk])
    h5f.close()
    h5f1.close()