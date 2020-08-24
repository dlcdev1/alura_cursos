import { UserService } from "./user.service";
import { TokenService } from "../token/token.service";
import { TestBed } from "@angular/core/testing";

describe('O serviço UserService', () => {
    let service:UserService;
    
    beforeEach(() => {
        TestBed.configureTestingModule({
            providers:[UserService]
        });
        service = TestBed.get(UserService);
    })

    it('O serviço user service deve ser instanciado', () => {
        expect(service).toBeTruthy();
    });
    it('Deve através de um token, recuperar as informações do usuario', () => {
        const token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwibmFtZSI6ImZsYXZpbyIsImVtYWlsIjoiZmxhdmlvQGFsdXJhcGljLmNvbS5iciIsImlhdCI6MTU5NTYxOTYyNCwiZXhwIjoxNTk1NzA2MDI0fQ.dzKUA6dIG5PaO6xmbbngOH5u_7iDo13-UV9ZqqoVQrA";
        service.setToken(token);
        expect(service.isLogged).toBeTruthy();
        expect(service.getUserName()).toBe('flavio');
        service.getUser().subscribe(user => {
            expect(user.name).toBe('flavio');
        });
    });

    it('dev limpara as informações no logout', () => {
        const token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwibmFtZSI6ImZsYXZpbyIsImVtYWlsIjoiZmxhdmlvQGFsdXJhcGljLmNvbS5iciIsImlhdCI6MTU5NTYxOTYyNCwiZXhwIjoxNTk1NzA2MDI0fQ.dzKUA6dIG5PaO6xmbbngOH5u_7iDo13-UV9ZqqoVQrA";
        service.setToken(token);
        service.logout();
        expect(service.isLogged()).toBeFalsy();
        expect(service.getUserName()).toBe('');
    })

});