from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CadastroUsuarioForm, EquipamentoForm
from .models import Equipamento


def cadastro_usuario(request):
    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":
        form = CadastroUsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            messages.success(request, "Perfil criado com sucesso!")
            return redirect("dashboard")
    else:
        form = CadastroUsuarioForm()

    return render(request, "meu_app/cadastro_usuario.html", {"form": form})


@login_required
def dashboard(request):
    equipamentos = Equipamento.objects.all()

    contexto = {
        "equipamentos": equipamentos[:5],
        "total_equipamentos": equipamentos.count(),
        "total_em_uso": equipamentos.filter(em_uso=True).count(),
        "total_disponiveis": equipamentos.filter(em_uso=False).count(),
    }

    return render(request, "meu_app/dashboard.html", contexto)


@login_required
def lista_equipamentos(request):
    equipamentos = Equipamento.objects.all()

    return render(
        request,
        "meu_app/lista.html",
        {"equipamentos": equipamentos}
    )


@login_required
def cadastrar_equipamento(request):
    if request.method == "POST":
        form = EquipamentoForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Equipamento cadastrado com sucesso!"
            )

            return redirect("lista_equipamentos")

    else:
        form = EquipamentoForm()

    return render(
        request,
        "meu_app/cadastro_equipamento.html",
        {"form": form}
    )


@login_required
def detalhes_equipamento(request, id):
    equipamento = get_object_or_404(
        Equipamento,
        id=id
    )

    return render(
        request,
        "meu_app/detalhes.html",
        {"equipamento": equipamento}
    )


@login_required
def perfil(request):
    return render(
        request,
        "meu_app/perfil.html"
    )


@login_required
def excluir_equipamento(request, id):
    equipamento = get_object_or_404(
        Equipamento,
        id=id
    )

    if request.method == "POST":
        equipamento.delete()

        messages.success(
            request,
            "Equipamento excluído com sucesso!"
        )

        return redirect("lista_equipamentos")

    return redirect(
        "detalhes_equipamento",
        id=id
    )