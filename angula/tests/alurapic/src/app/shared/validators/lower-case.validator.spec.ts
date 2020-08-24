import { isLowerCase } from "./lower-case.validator";

describe('A função isLowerCase', () =>{

    it('A função de retornar verdadeiro para texto em caixa baixa', () => {
        const valor = 'bolinha';
        const result = isLowerCase(valor);

        expect(result).toBeTruthy();
    });

    it('A função de retornar falso para texto em caixa alta', () => {
        const valor = 'Bolinha';
        const result = isLowerCase(valor);
        expect(result).not.toBeTruthy();
    });

});