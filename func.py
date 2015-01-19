import os, pickle

class Function(object):

    def __init__(self, fn, _locals=None):
        self.fn = fn
        self.cn = 0
        self.locals = _locals or {}

    def __call__(self, *args, **kwargs):
        kwargs.update(self.locals)

        filename = 'f{}.pck'.format(self.cn)
        pck = open(filename, 'wb')
        pickle.dump(args, pck)
        pickle.dump(kwargs, pck)
        pck.close()

        out = 'import pickle\n'
        out += 'pck = open("{}", "rb")\n'.format(filename)
        out += 'args = pickle.load(pck)\n'
        out += 'kwargs = pickle.load(pck)\n'
        out += 'pck.close()\n'
        out += 'for i, val in enumerate(args):\n'
        out += '    locals()["arg{}".format(i)] = val\n'
        out += self.fn

        mod_filename = 'f{}'.format(self.cn)
        py = mod_filename + '.py'
        pyc = py + 'c'

        fi = open(py, 'w')
        fi.write(out)
        fi.close()

        module = __import__(mod_filename)
        if not os.path.isfile(pyc):
            reload(module)

        try:
            rv = module.result
        except AttributeError:
            rv = None

        os.remove(py)
        os.remove(pyc)
        os.remove(filename)
        self.cn += 1
        return rv

    def __repr__(self):
        return self.fn