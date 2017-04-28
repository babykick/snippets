import win32com.client


def readJsFile(filename):
    fp = file( filename, 'r' )
    lines = ''
    for line in fp:
        lines += line
    return lines


def driveJsCode(code, func, paras=None):
    js = win32com.client.Dispatch('MSScriptControl.ScriptControl')
    js.Language = 'JavaScript'
    js.AllowUI  = False
    js.AddCode( code )
    if paras:
        return js.Run(func, paras[0], paras[1])
    else:
        return js.Run(func)

        
if __name__ == '__main__':
    code = readJsFile( 'comm.js' )
    p = driveJsCode( code, 'myPreProcess', [password, verfcode] )
    print 'The decoded code is %s' % p
