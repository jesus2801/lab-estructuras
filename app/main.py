import eel
import screen1

@eel.expose
def pythonIsWorking():
    print('eel working correctly.')
    return


if __name__ == '__main__':
    eel.init('web')
    eel.start('main.html', size=(1280, 720), port=3000, mode='chrome')
