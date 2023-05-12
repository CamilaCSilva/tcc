import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { PerfilService } from './perfil.service';
import { PerfilInfo } from '../models/perfil.model';

@Component({
  selector: 'app-perfil',
  templateUrl: './perfil.component.html',
  styleUrls: ['./perfil.component.scss']
})
export class PerfilComponent implements OnInit {

  path: string = 'perfil/editar-perfil';
  string = 'Perfil';
  testResult: boolean = false;
  perfil: PerfilInfo;

  usuario: any = {
    nome: 'Isabela',
    funcao: 'Profissional de Saúde',
    docmentro_trabalho: 78965,
    cpf: '78965412320',
    unidade_atendimento: 'Hospital Antônio Moreira da Costa',
    celular: '(35)99123-4567'
  };

  constructor(private router: Router, private perfilService: PerfilService) { }

  ngOnInit(){
    this.listarProfissional();
  }

  listarProfissional(){
    this.perfilService.getPerfilInfo(this.usuario.cpf).subscribe(perfilInfo => {
    this.perfil = perfilInfo;
    if(this.perfil?.campo_escolha == 'CRM') { this.perfil.campo_escolha = 'Médico(a)'; }
    else if(this.perfil?.campo_escolha == 'COREN') { this.perfil.campo_escolha = 'Enfermeiro(a)'; }
    else if(this.perfil?.campo_escolha == 'DRF') { this.perfil.campo_escolha = 'Paramédico(a)'; }
    }, err => {
      console.log('Erro ao listar o profissional', err)
    })
  }

  editar(){
    this.router.navigateByUrl(this.path);
  }
}
