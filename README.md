# WinLocker-007
Rewritten version the [WinLocker-007](https://github.com/pro100git/WinLocker-007/tree/master/rewritten_007)
![alt tag](https://github.com/pro100git/WinLocker-007/blob/master/Screenshot_1.jpg "007")​

#### Зависимости | Requirements
* python==3.7
* keyboard==0.13.5
* psutil==5.7.2

#### Описание
Хитрость WinLocker-007 в том, что стандартное подтверждение пароля по клавише ENTER не сработает, даже если он будет правильным, вместо этого, пароль принимается по сочетанию клавишь **Alt-s** (можно изменить, 34 строка). Для работы нужно создать файл pas.txt и вписать туда свой пароль, на 21 строке указать путь к файлу.

#### Блокировка клавишь
* Del
* Esc
* Windows
* Tab

#### Блокировка приложений
* taskmgr.exe
* cmd.exe
* powershell.exe
* powershell_ise.exe
* regedit.exe
* mmc.exe
* msconfig.exe
* ProcessHacker.exe
* iexplore.exe
* game.exe
